#!/usr/bin/env python
# coding=utf-8
import subprocess
import sys
import time

from machinekit import launcher
import rospy

try:
    launcher.register_exit_handler()  # enable on ctrl-C, needs to executed after HAL files
    path = rospy.get_param('/hal_config_path', '')
    launcher.start_process('mklauncher')
    launcher.start_process('configserver -n Borunte-Control {}'.format(path))

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)
