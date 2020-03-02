cmake_minimum_required(VERSION 2.8.3)
project(borunte_robot)

find_package(
    catkin REQUIRED
)

catkin_package(CATKIN_DEPENDS borunte_support borunte_moveit_config borunte_hal)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
