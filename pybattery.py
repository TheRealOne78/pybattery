#!python3

## Copyright_notice ####################################################
#                                                                      #
# SPDX-License-Identifier: GPL-3.0-or-later                            #
#                                                                      #
# Copyright (C) 2024 TheRealOne78 <bajcsielias78@gmail.com>            #
# This file is part of the PyBattery project                           #
#                                                                      #
# PyBattery is free software: you can redistribute it and/or modify    #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License,       #
# or (at your option) any later version.                               #
#                                                                      #
# PyBattery is distributed in the hope that it will be useful, but     #
# WITHOUT ANY WARRANTY; without even the implied warranty of           #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU    #
# General Public License for more details.                             #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with PyBattery. if not, see <http://www.gnu.org/licenses/>.    #
#                                                                      #
########################################################################

"""
A python script changing Android battery level with adb, alternating between 2%
and 1000%
"""


### IMPORT ###

import os         # import os to adb
import time       # import time to sleep
import subprocess # import subprocess to check for adb
import signal     # import signal to handle signals
import sys        # import sys for getopt
import getopt     # import getopt for arguments
import logging    # import logging


### CONFIG CONSTANTS ###

## WARNING! ####################################################
#  'min_range' and 'i' must NOT be set to less than 2!         #
#  Otherwise, some phones will shut down and even softlock!!!  #
#  Set ranges wisely.                                          #
################################################################

SLEEP     = 0.05
MIN_RANGE = 2    # See the warning message from above!!!
MAX_RANGE = 1000


### CONSTANTS ###

PROJECT_NAME   = "PyBattery"
VERSION_STRING = "1.2.0"


### FUNCTIONS ###

def print_help():
   """
   Print a help message
   """

   help_message = ('%s\n'
                   'A python script changing Android battery level with adb,\n'
                   'alternating between 2% and 1000%\n'
                   '\n'
                   'Usage: %s [options]\n'
                   '\n'
                   'Options:\n'
                   '-h, --help          Output this help list and exit\n'
                   '-v, --version       Output version information and license and exit\n'
                   '-D, --debug         Output the debug log\n'
                   '-s, --set-level     Set battery level\n'
                   '-r, --reset-level   Reset battery level',
                   PROJECT_NAME, sys.argv[0])

   print(help_message)


def print_version():
   """
   Print version
   """

   version_message = ('%s version %s\n'
                      '\n'
                      'Copyright (C) 2024 TheRealOne78\n'
                      'License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/agpl.html>.\n'
                      'This is free software: you are free to change and redistribute it.\n'
                      'There is NO WARRANTY, to the extent permitted by law.',
                      PROJECT_NAME, VERSION_STRING)

   print(version_message)


def handle_signal(signum, frame):
    """
    Handle signals by resetting the battery and gracefully exiting
    """

    exit(reset_level())



def command_exists(command):
    """
    Check if a specific command exists and can be executed
    """

    try:
        subprocess.check_output(['which', command])
        return True
    except subprocess.CalledProcessError:
        return False


## Set battery level
def set_level(level):
    """
    Set battery level through `adb`

    'level' contains an integer type value which will be used to set the battery level
    """

    os.system(f"adb shell dumpsys battery set level {level}")
    print(f"{PROJECT_NAME}> {level}%")
    time.sleep(SLEEP)


## Set battery level
def reset_level():
    """
    Reset battery level through `adb`

    RETURN: Error status - 0 if OK, non-zero if an error occurred
    """

    # Check if adb exists
    if not command_exists("adb"):
        logging.error("`adb' cannot be found on this system. Please install `adb' in order to use pybattery.")
        exit(1)

    logging.info("\nRestoring battery level to normal...")

    # Reset battery level with `adb` and get the exit code
    exit_code = os.system("adb shell dumpsys battery reset")

    if exit_code != 0:
        logging.error("Couldn't reset battery level. Please run `adb shell dumpsys battery reset` manually or reboot your device.")

        if exit_code > 255:
            exit_code = 1

    else:
        logging.info("Done.")

    return exit_code


def main():
    """
    main
    """

    # Register the signal handler
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    # Turn on info logging by default
    logging.basicConfig(level=logging.INFO)

    # Get arguments
    opts, args = getopt.getopt(sys.argv[1:], "hvDs:r", ['help', 'version', 'debug', 'set-level=', 'reset-level'])

    # Handle options
    for opt, arg in opts:
        if opt in   ('-h', '--help'):        # Print a help message and exit gracefully
            print_help()
            sys.exit(0)

        elif opt in ('-v', '--version'):     # Print version & licensing and exit gracefully
            print_version()
            sys.exit(0)

        elif opt in ('-D', '--debug'):       # Turn on debug logging
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("Turned on debug logging")

        elif opt in ('-s', '--set-level'):   # Set battery level with `adb`
            set_level(arg)
            exit(0)

        elif opt in ('-r', '--reset-level'): # Reset battery level with `adb`
            exit(reset_level())

    # Check if adb exists
    if not command_exists("adb"):
        logging.error("`adb' cannot be found on this system. Please install `adb' in order to use pybattery.")
        exit(1)

    # increment/decrement battery level in an infinite loop fashion
    current_level = MIN_RANGE
    while True:
        while (current_level < MAX_RANGE):
            set_level(current_level)
            current_level += 1
        while (current_level > MIN_RANGE):
            set_level(current_level)
            current_level -= 1


### START ###
if __name__ == "__main__":
   main()
