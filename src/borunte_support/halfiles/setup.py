# coding=utf-8
import os
import sys
import time

import rospy
from machinekit import launcher
from machinekit import rtapi as rt
from machinekit import hal

NUM_JOINTS = 6

HAL_CONFIG_PATH = rospy.get_param('/hal_config_path', '')
sys.path.append(HAL_CONFIG_PATH)
os.environ['PYTHONPATH'] += ':{}'.format(HAL_CONFIG_PATH)


def install_rt_comps():
    launcher.install_comp(
        os.path.join(HAL_CONFIG_PATH, 'components', 'absolute_joint.icomp')
    )


def create_hw_interface(thread):
    rt.loadrt('{}/hal_hw_interface'.format(os.environ['COMP_DIR']))
    hal.addf('hal_hw_interface', thread.name)

def connect_hw_interface():
    for nr in range(1, NUM_JOINTS + 1):
        hal.Pin('hal_hw_interface.joint_{}.pos-cmd'.format(nr)).link(
            'joint-{}-cmd-pos'.format(nr)
        )
        hal.Pin('hal_hw_interface.joint_{}.pos-fb'.format(nr)).link(
            'joint-{}-fb-out-pos'.format(nr)
        )


def setup_hal():
    sim = rospy.get_param('/sim_mode', True)
    if sim:
        os.environ['SIM_MODE'] = '1'

    from borunte_hal.robot import setup_thread, configure_hal

    cgname = rospy.get_param('/hal_mgr/hal_cgroup_name')
    thread = setup_thread(cgname)
    create_hw_interface(thread)
    configure_hal(thread)
    time.sleep(1.0)
    connect_hw_interface()


install_rt_comps()
setup_hal()
