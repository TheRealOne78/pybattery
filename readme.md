# PyBattery

A python code that will change your android phone battery level from 2-1000

To use this, you need to have linux installed

Install adb with `(sudo) apt install adb`. A internet connection is required.

Install as well python3 to run this py file with `(sudo) apt install python3`. Again, a internet connection is required to install python3.

Run the code with `python3 ./pybattery.py`.

Note that you need to trigger usb debbuging in developer options in your phone you want to experiment this.

In case you want to restore the battery level to normal, use `adb adb shell dumpsys battery restore` or just restart your phone.

I am not responsible for any damage to your devices. Experiment with your own risk!
