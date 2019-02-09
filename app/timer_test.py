import time
from libs.SevenSegment import SevenSegment


def countdown(t):
    display = SevenSegment()
    display.begin()
    colon = True

    next_call = time.time()

    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}{:02d}'.format(mins, secs)
        display.print_float(float(timeformat))
        display.set_colon(colon)
        display.write_display()
        t -= 1

        time.sleep(max(0, next_call - time.time()))

countdown(3600)
