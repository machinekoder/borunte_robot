#!/usr/bin/env python
# -*- coding: utf-8 -*-
# very small helper script for short-cutting
# input and output pins when passing data
# thru HAL shared memory setup
import sys
import time
import subprocess

from machinekit import launcher
from machinekit import hal

try:
    launcher.check_installation()
    launcher.cleanup_session()  # kill any running Machinekit instances
    launcher.start_realtime()  # start Machinekit realtime environment

    while 'ul_iface_component.joint_6.pos-cmd' not in hal.pins:
        time.sleep(0.5)

    print('found HAL pin, connecting')
    # create 6 signals between pos-cmd and pos-fb pins
    # when machinekit_ros_control has started with
    # parameter machinekit_interface: 0
    for i in range(1, 7):
        hal.Pin('ul_iface_component.joint_%s.pos-cmd' % i).link(
            'ul_iface_component.joint_%s.pos-fb' % i
        )

    launcher.register_exit_handler()  # enable on ctrl-C, needs to executed after HAL files

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

sys.exit(0)
