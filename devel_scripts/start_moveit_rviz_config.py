#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sh import roslaunch

from launcher import start_process, terminate_processes, wait_loop

if __name__ == '__main__':
    start_process(
        roslaunch,
        'borunte_moveit_config borunte_moveit_config.launch rviz:="true"',
    )
    wait_loop()
    terminate_processes()
