cmake_minimum_required(VERSION 2.8.3)
project(borunte_moveit_config)

find_package(catkin REQUIRED COMPONENTS
    borunte_support
)

catkin_package(
    CATKIN_DEPENDS borunte_support
)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
