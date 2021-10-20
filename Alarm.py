import datetime
from pygame import mixer
from time import sleep, time
mixer.init()


class Alarm:

    def __init__(self):
        self.music_list = {'sound of water': 'media/1.mp3', 'birdsong': 'media/2.mp3',
                           'noise of nature': 'media/3.mp3', 'just alarm': 'media/4.mp3'}

    def time_equal(self, d, h, m):
        while True:
            time_now = datetime.datetime.now()
            if str(time_now.day) == d and str(time_now.hour) == h and str(time_now.minute) == m:
                return True
            sleep(2)

    def set_alarm(self, d, h, m, x):
        if self.time_equal(d, h, m) == True:
            self.music_load(x)

    def music_load(self, x):

        mixer.music.load(self.music_list[x])
        mixer.music.play()
        return mixer.music.get_busy()

    def music_stop(self):
        mixer.music.stop()
        return mixer.music.get_busy()
