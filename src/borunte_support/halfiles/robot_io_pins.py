# -*- coding: utf-8 -*-

import rospy
from machinekit import hal


def setup_sim_pins():
    rospy.loginfo('Creating io-rcomp HAL remote component')
    # mirror hal_io to rcomp
    hal_io = hal.components['hal_io']
    rcomp = hal.RemoteComponent('io-rcomp', timer=100)
    for pin in hal_io.pins():
        name = '.'.join(pin.name.split('.')[1:])
        if not name.startswith('digital_'):
            continue
        dir_map = {hal.HAL_IN: hal.HAL_OUT, hal.HAL_OUT: hal.HAL_IN}
        rcomp.newpin(name, pin.type, dir_map.get(pin.dir, hal.HAL_IO))
        if pin.linked:
            continue
        if pin.dir == hal.HAL_IN:
            rcomp.pin(name).link(hal.pins[pin.name])
        else:
            hal.pins[pin.name].link(rcomp.pin(name))
    rcomp.ready()


def setup_gripper_pins():
    hal.Pin('hal_io.digital_out_1').link('gripper-open-close')
    hal.Pin('hal_io.digital_in_1').link('gripper-opened')


def setup_robot_control_pins():
    hal.Pin('hal_io.state_cmd').link(hal.Signal('state-cmd'))
    hal.Pin('hal_io.state_fb').link(hal.Signal('state-fb'))
    hal.Pin('hal_io.reset').link(hal.Signal('reset-in'))


def setup_pins():
    sim = rospy.get_param('/sim_mode', True)
    setup_gripper_pins()
    if sim:
        setup_sim_pins()
    setup_robot_control_pins()


setup_pins()
