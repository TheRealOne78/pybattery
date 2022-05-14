# PyBattery

A python code that will change android device battery level, looping from 1% to 1000% and back.

### Dependencies

In **Linux** distributions, install `adb` on:<br>
 - **Debian** based distros with `(sudo) apt install adb`<br>
 - **Arch** based distros with `(sudo/doas) pacman -S adb`<br>
 - **Gentoo** with `(sudo/doas) emerge adb`<br>
Ps: An internet connection is required for this step.

In **Linux** distributions, install as well `python2` or `python3` in order to run this python file:
 - **Debian** based distros with `[sudo] apt install python3`<br>
 - **Arch** based distros with `[sudo/doas] pacman -S python3`<br>
 - **Gentoo** with `[sudo/doas] emerge -a dev-lang/python`<br>
Ps: An internet connection is required for this step.

In **Windows** or **macOS** cases, `adb` and `python` still need to be installed in order for functionality.

### Download

There are 3 options:
  1. Download the git repository by cloning it with `git clone https://github.com/TheRealOne78/pybattery.git`</li>
  2. Download a zip file from https://github.com/TheRealOne78/pybattery/archive/refs/heads/main.zip or clicking the `Code`>`Download ZIP` buttons in GitHub</li>
  3. Copy or download the code from https://github.com/TheRealOne78/pybattery/blob/main/pybattery.py or clicking the `pybattery.py` in GitHub and copying/downloading the source code</li>

### How to run
In the Android device, `USB Debbuging` in Developer Options needs to be activated in order for `adb` to reach and send commands to the Android device.

In **Linux** and **macOS** run the python file with `python3 ./pybattery.py`.
In Windows double click pybattery.py to execute it via python.

For restoring the battery level to normal, `adb shell dumpsys battery restore` needs to be executed or an Android reboot.

### Disclaimer and License
Copyright (C) 2022 TheRealOne78<br>
License GPLv3+: GNU GPL version 3 or later https://gnu.org/licenses/gpl.html.<br>
This is free software: you are free to change and redistribute it.<br>
There is NO WARRANTY, to the extent permitted by law.<br>

<b>I am not responsible for any damage to your devices. Experiment with your own risk!</b>
