# PyBattery

A python code that will change android device battery level, looping from 1% to 1000% and back.

### Dependencies

In **GNU/Linux** distributions, install `adb` on:
 - **Debian** based distros with `(sudo) apt install adb`
 - **Arch** based distros with `(sudo/doas) pacman -S adb`
 - **Gentoo** with `(sudo/doas) emerge adb`<br>
Ps: An internet connection is required for this step.

In **Linux** distributions, install as well `python2` or `python3` in order to run this python file:
 - **Debian** based distros with `[sudo] apt install python3`
 - **Arch** based distros with `[sudo/doas] pacman -S python3`
 - **Gentoo** with `[sudo/doas] emerge -a dev-lang/python`<br>
Ps: An internet connection is required for this step.

In **Windows** or **macOS**, `adb` and `python` need to be installed. See https://developer.android.com/tools/adb and https://www.python.org/downloads/ for more info.

### Download

There are 3 main methods to download the source code:
  1. By downloading the git repository by cloning it with `git clone https://github.com/TheRealOne78/pybattery.git`;
  2. By downloading a zip file from https://github.com/TheRealOne78/pybattery/archive/refs/heads/main.zip or clicking the `Code`>`Download ZIP` buttons in GitHub;
  3. Or by copying/downloading the source code from https://github.com/TheRealOne78/pybattery/blob/main/pybattery.py or clicking the `pybattery.py` in GitHub and copying/downloading the source code.

### How to run
In the Android device, `USB Debbuging` in Developer Options needs to be activated in order for `adb` to reach and send commands to the Android device.

In **Linux** and **macOS** run the python file with `python3 ./pybattery.py`.
In Windows double click pybattery.py to execute it via python.

For restoring the battery level to normal, `adb shell dumpsys battery restore` needs to be executed or Android has to be rebooted.

### Disclaimer and License
Copyright (C) 2022 TheRealOne78<br>
License GPLv3+: GNU GPL version 3 or later https://gnu.org/licenses/gpl.html.<br>
This is free software: you are free to change and redistribute it.<br>
There is NO WARRANTY, to the extent permitted by law.<br>

**I am not responsible for any damage to your devices. Experiment at your own risk!**
