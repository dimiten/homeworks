from text import Text
from image import Image
from video import Video


if __name__ == "__main__":
    text_1 = Text(name="text_1", extension="txt", size=20, description="text file", modified=0, data="text_1 data")
    text_1.write_in_file("test data for text")
    print(text_1.read_from_file())

    image_1 = Image(name="image_1", extension="img", size=30, description="image file", modified=0, data="image_1 data",
                    dimension=50)
    image_1.write_in_file("test data for image")
    print(image_1.read_from_file())

    video_1 = Video(name="video_1", extension="mp4", size=40, description="video file", modified=0, data="video_1 data",
                    dimension=50, length=100)
    video_1.write_in_file("test data for video")
    print(video_1.read_from_file())



