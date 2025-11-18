class Video:
    def create(self, name: str) -> None:
        self.name = name

    def play(self) -> str:
        if not self.name:
            raise AttributeError("Название видео не задано!")
        print(f"воспроизведение видео {self.name}")
    

class YouTube:
    videos = []
    @classmethod
    def add_video(cls, video: Video) -> None:
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int) -> None:
        cls.videos[video_indx].play()


v1 = Video()
v1.create("Python")

v2 = Video()
v2.create("Python ООП") 

for video in (v1, v2):
    YouTube.add_video(video)

YouTube.play(0)
YouTube.play(1)
