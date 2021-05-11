import os   #import os to adb
import time #import time to sleep

i = 2

while True:
    while (i < 1000):
        n = str(i)
        os.system('adb shell dumpsys battery set level ' + n)
        time.sleep(0.05)
        i = i + 1
    while (i > 2):
        n = str(i)
        os.system('adb shell dumpsys battery set level ' + n)
        time.sleep(0.05)
        i = i - 1
