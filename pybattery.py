#!python

import os         # import os to adb
import time       # import time to sleep
import subprocess # import subprocess to check for adb
import signal     # import signal to handle signals

## WARNING! ####################################################
#  'min_range' and 'i' must NOT be set to less than 2!         #
#  Otherwise, some phones will shut down and even softlock!!!  #
#  Set ranges wisely.                                          #
################################################################

sleep = 0.05
min_range = 2
max_range = 1000
i = min_range


## Signal handler
def handle_signal(signum, frame):
    print("\nRestoring battery level to normal...")
    exit_code = os.system("adb shell dumpsys battery reset")
    if exit_code == 0:
        print("Done.")
    else:
        print("Couldn't reset battery level. Please run `adb shell dumpsys battery reset` manually or reboot your device.")
    print("Exiting...")
    if exit_code > 255:
        exit_code = 1
    exit(exit_code)


## Checks is adb exists
def command_exists(command):
    try:
        subprocess.check_output(['which', command])
        return True
    except subprocess.CalledProcessError:
        return False


## Set battery level
def set_level():
    os.system("adb shell dumpsys battery set level {}".format(i))
    print("pybattery> {}%".format(i))
    time.sleep(sleep)


## Register the signal handler
signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)


## Check if adb exists
if not command_exists("adb"):
    print("adb does not exist in this system. Please install adb in order to use pybattery.")
    exit(1)


## Set battery infinitely
while True:
    while (i < max_range):
        set_level()
        i = i + 1
    while (i > min_range):
        set_level()
        i = i - 1
