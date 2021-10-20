import time


class Clock:

    def format_clock(self):

        hour_display = time.strftime("%H")
        minute_display = time.strftime("%M")
        second_display = time.strftime("%S")
        text_display = hour_display + ":" + minute_display + ":" + second_display
        return str(text_display)
