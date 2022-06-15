import json
import math


class Frame:
    def __init__(self, vid_num, frame_num, parent_path):
        self.vid_num = vid_num
        self.frame_num = frame_num
        self.parent_path = parent_path
        self.file_path = self.get_file_path()
        self.pose = self.get_pose()
        self.ratio = self.get_ratio()
        self.angle = self.get_angle()
        self.velocity = self.get_velocity()
        self.fall = self.detect_fall()

    def __str__(self):
        return f"Frame object of video {self.vid_num}, frame {self.frame_num}"

    def get_file_path(self):
        file_path_relative = f"/video_{self.vid_num}/data {self.vid_num} ({self.frame_num}).json"
        return (self.parent_path + file_path_relative)

    def get_pose(self):
        file_data = json.load(open(self.file_path))
        if file_data == []:
            return []
        else:
            return file_data[0]["keypoints"]

    def get_ratio(self):
        if self.pose == []:
            return -1
        else:
            pose_x = []
            pose_y = []
            for item in self.pose:
                pose_x.append(item["x"])
                pose_y.append(item["y"])

            min_x_above_0 = min(i for i in pose_x if i > 0)
            min_y_above_0 = min(i for i in pose_y if i > 0)

            width = max(pose_x) - min_x_above_0
            height = max(pose_y) - min_y_above_0

            if height == 0:
                return -1
            else:
                return round(width / height, 2)

    def get_angle(self):
        if self.pose == []:
            return 181
        else:
            left_ankle = self.pose[-2]
            right_ankle = self.pose[-1]
            nose = self.pose[0]

            mid_ankle_x = (left_ankle["x"] + right_ankle["x"]) / 2
            mid_ankle_y = (left_ankle["y"] + right_ankle["y"]) / 2

            if nose["x"] == mid_ankle_x:
                return 181
            else:
                angle_in_radian = math.atan(
                    abs(nose["y"] - mid_ankle_y)/(nose["x"] - mid_ankle_x))
                angle_in_degree = abs(angle_in_radian * 180 / math.pi)
                return round(angle_in_degree, 2)

    def get_velocity(self):
        if (self.frame_num < 6) or (self.pose == []):
            return -1
        else:
            interval = 1 / 30 * 5
            prev_frame = Frame(
                self.vid_num, self.frame_num - 5, self.parent_path)

            if prev_frame.pose == []:
                return -1
            else:
                left_hip = self.pose[11]
                right_hip = self.pose[12]

                left_hip_prev_frame = prev_frame.pose[11]
                right_hip_prev_frame = prev_frame.pose[12]

                center_hip_y = (left_hip["y"] + right_hip["y"]) / 2
                center_hip_y_prev_frame = (
                    left_hip_prev_frame["y"] + right_hip_prev_frame["y"]) / 2

                center_hip_distance = abs(
                    center_hip_y - center_hip_y_prev_frame)
                center_hip_distance_in_meter = center_hip_distance * 0.0002645833
                velocity = center_hip_distance_in_meter / interval

                return round(velocity, 5)

    def detect_fall(self):
        if (self.velocity > 0.009) & (self.angle < 45) & (self.ratio > 1):
            return True
        else:
            return False
