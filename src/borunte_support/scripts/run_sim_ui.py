#!/usr/bin/env python
# coding=utf-8
import subprocess
import sys
import time

from machinekit import launcher
import rospkg

PACKAGE_NAME = 'borunte_support'

rospack = rospkg.RosPack()

try:
    launcher.register_exit_handler()  # enable on ctrl-C, needs to executed after HAL files
    launcher.ensure_mklauncher()  # ensure mklauncher is started
    launcher.start_process('configserver -n HAL-IO {}'.format(rospack.get_path(PACKAGE_NAME)))

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)
