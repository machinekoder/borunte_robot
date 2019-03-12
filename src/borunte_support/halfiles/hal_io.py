# -*- coding: utf-8 -*-
from machinekit import hal


def load_hal_io_component():
    # Load hal_io user component
    cmd = 'rosrun hal_hw_interface hal_io'
    hal.loadusr(cmd, wait=True, wait_name='hal_io', wait_timeout=10.0)


load_hal_io_component()
