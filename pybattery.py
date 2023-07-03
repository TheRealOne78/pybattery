import os  #import os to adb
import time  #import time to sleep

i = 0


def set_level():
    os.system("adb shell dumpsys battery set level {}".format(i))
    print("\U0001F50B:{}%".format(i))
    time.sleep(0.05)


while True:
    while (i < 100):
        set_level()
        i = i + 1
    while (i > 2):
        set_level()
        i = i - 1