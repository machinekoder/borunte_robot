# -*- coding: utf-8 -*-
from machinekit import hal


def load_hal_io_component():
    # Load hal_io user component
    hal.loadusr('hal_io', wait=True)


load_hal_io_component()
