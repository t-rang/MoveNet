from video_model import Video


class Dataset:
    def __init__(self, path, start, end):
        self.path = path
        self.start = start
        self.end = end
        self.fall = self.get_fall()

    def get_fall(self):
        fall = []
        for i in range(self.start, self.end+1):
            video = Video(i, self.path)
            fall.append(video.fall)
        return fall
