import sys
from PathConstants import *
from Video import Video

class YoutubeConverter():
    """This is the main class for the Youtube to mp3 converter"""
    # param file:= list of video urls
    #param quality:= video quality, standart is 360p
    def __init__(self, queue_file, quality='360p'):
        self.quality = quality
        self.video_urls = self.parse_videoUrls()
        print self.video_urls
        self.video_index = 0

    # param file:= list of video urls
    #This method parses all urls in the given file and returns an array with all urls without the
    #'\n' character
    def parse_videoUrls(self):
        video_urls = [line.rstrip('\n') for line in open(QUEUE)]
        return video_urls

    def run(self):
        for video_url in self.video_urls:
            youtube_video = Video(video_url, self.video_index)

            print("Downloading %(title)s" % {"title": video.title}).encode('utf8')
            self.download_video(youtube_video)

            self.video_index += 1

    def download_video(video):
        stream = video.video_instance.streams.filter(res=quality, file_extension="mp4").first()
        stream.download(TEMP, video.tmp_name)


if __name__ == '__main__':
    if sys.version_info[0] != 2 or sys.version_info[1] < 7:
        print("This project requires at least Python 2.7")
        sys.exit(1)


    converter = YoutubeConverter(QUEUE)
    converter.run()
