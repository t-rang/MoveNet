from frame_model import Frame
import os


class Video:
    def __init__(self, vid_num, parent_path):
        self.vid_num = vid_num
        self.parent_path = parent_path
        self.frame_count = self.get_frame_count()
        self.frame_list = self.get_frame_list()
        self.fall = self.detect_fall()

    def __str__(self):
        return f"Video object of video {self.vid_num}"

    def get_frame_count(self):
        video_path = f"{self.parent_path}/video_{self.vid_num}"
        video_list_file = os.listdir(video_path)
        return(len(video_list_file))

    def get_frame_list(self):
        frame_list = []
        for i in range(1, self.frame_count):
            frame_list.append(Frame(self.vid_num, i, self.parent_path))
        return frame_list

    def detect_fall(self):
        frame_fall_list = []
        for item in self.frame_list:
            frame_fall_list.append(item.fall)
        if True in frame_fall_list:
            return 1
        else:
            return 0
