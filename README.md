# PyBattery

A Python-based application that will change android device battery level, looping from 2% to 1000% and viceversa.

### Dependencies

#### [adb - Android Debug Bridge](https://developer.android.com/tools/adb)

In **GNU/Linux** distributions, install `adb` on:
 - **Debian** based distros with `(sudo) apt install [adb](https://packages.debian.org/search?keywords=adb&searchon=names&suite=all&section=all)`
 - **Arch** based distros with `(sudo/doas) pacman -S [android-tools](https://archlinux.org/packages/extra/x86_64/android-tools)`
 - **Gentoo** with `(sudo/doas) emerge [dev-util/android-sdk-update-manager](https://packages.gentoo.org/packages/dev-util/android-sdk-update-manager)`<br>

In **Apple macOS**, install `adb` by:
 - Installing with [homebrew](https://brew.sh), using `brew install android-platform-tools`
 - Or by manually installing it from https://developer.android.com/tools/adb

In **Microsoft Windows**, install `adb` from [https://developer.android.com/tools/adb](https://developer.android.com/tools/adb).

#### [Python](https://www.python.org/)

In **GNU/Linux** distributions, install `python` on:
 - **Debian** based distros with `[sudo] apt install [python3](https://packages.debian.org/search?suite=all&section=all&arch=any&searchon=names&keywords=python3)`
 - **Arch** based distros with `[sudo/doas] pacman -S [python](https://archlinux.org/packages/core/x86_64/python)`
 - **Gentoo** with `[sudo/doas] emerge -a [dev-lang/python](https://packages.gentoo.org/packages/dev-lang/python)`<br>

In **Apple macOS**, install `python` from [https://www.python.org/downloads](https://www.python.org/downloads).

In **Microsoft Windows**, install `python` from [https://www.python.org/downloads](https://www.python.org/downloads).

### Download

There are 3 main methods to download the source code:
  1. By downloading the git repository by cloning it with `git clone https://github.com/TheRealOne78/pybattery.git`;
  2. By downloading a zip file from https://github.com/TheRealOne78/pybattery/archive/refs/heads/main.zip or clicking the `Code`>`Download ZIP` buttons in GitHub;
  3. Or by copying/downloading the source code from https://github.com/TheRealOne78/pybattery/blob/main/pybattery.py or clicking the `pybattery.py` file in GitHub and copying/downloading the source code.

### How to run
In the Android device, `USB Debbuging` in Developer Options needs to be activated in order for `adb` to reach and send commands to the Android device.

In **Linux** and **macOS** run the python file with `python3 ./pybattery.py`.
In Windows double click pybattery.py to execute it via python.

For restoring the battery level to normal, `adb shell dumpsys battery reset` needs to be executed or Android has to be rebooted.

### Disclaimer and License
Copyright (C) 2023 TheRealOne78<br>
License GPLv3+: GNU GPL version 3 or later [https://gnu.org/licenses/gpl.html](https://gnu.org/licenses/gpl.html).<br>
This is free software: you are free to change and redistribute it.<br>
There is NO WARRANTY, to the extent permitted by law.<br>

**I am not responsible for any damage to your devices. Experiment at your own risk!**
