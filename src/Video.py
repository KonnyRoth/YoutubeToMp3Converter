import pytube
import urlparse
from PathConstants import TEMP
import os

class Video():
    """This class represets a youtube video"""

    # param url:= represents the url to the video
    # param index:= index of temporary name
    def __init__(self, url, index):
        self.url = url
        self.video_instance = pytube.YouTube(str(self.url))
        self.title = self.video_instance.title
        self.thumbnail_url = get_thumbnail()
        self.tmp_name = 'tmp_file_%(video_index)d' % {'video_index': index} #temporary filename

    #return: concatenated string which is the url to the video thumbnail
    #This method extracts the video id from the url and concatenates it
    #with youtubes url to the thumbnail
    def get_thumbnail(self):
        video_id = urlparse.urlparse(self.url)
        query = urlparse.parse_qs(video_id.query)
        video_id = query['v'][0]

        return "http://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"
