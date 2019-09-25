cmake_minimum_required(VERSION 2.8.3)
project(borunte_moveit_config)

add_compile_options(-std=c++11)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(catkin REQUIRED COMPONENTS
    borunte_support
    moveit_ros_move_group
    rosparam_shortcuts
    std_msgs
    tf
    tf_conversions
)

find_package(Eigen3 REQUIRED)
find_package(OMPL REQUIRED)
find_package(moveit_planners_ompl REQUIRED)

catkin_package(
    CATKIN_DEPENDS
    borunte_support
    roscpp
    moveit_ros_move_group
    moveit_ros_planning_interface
    tf
    tf_conversions
)

include_directories(include ${catkin_INCLUDE_DIRS} ${Eigen_INCLUDE_DIRS})

add_executable(construct_state_database src/construct_state_database.cpp)
add_dependencies(construct_state_database ${catkin_EXPORTED_TARGETS})
target_link_libraries(construct_state_database ${moveit_planners_ompl_LIBRARIES} ${OMPL_LIBRARIES} ${catkin_LIBRARIES} ${Boost_LIBRARIES})

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
