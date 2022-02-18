# PyBattery

A python code that will change your android phone battery level from 2-1000

To use this, you need to have linux installed

Install adb on: 
debian based distros with `sudo apt install adb`. 
arch based distros with `sudo pacman -S adb`.
gentoo with `sudo emerge adb`.
Internet connection is required for this.

Install as well python3 to run this py file with `(sudo) apt install python3`. Again, an internet connection is required to install python3.

Run the code with `python3 ./pybattery.py`.

Note that you need to trigger usb debbuging in developer options in your phone if you want to experiment with this.

In case you want to restore the battery level to normal, use `adb shell dumpsys battery restore` or just restart your phone.

<b>I am not responsible for any damage to your devices. Experiment with your own risk!</b>
