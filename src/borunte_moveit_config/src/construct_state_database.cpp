#include <moveit/ompl_interface/ompl_interface.h>
#include <moveit/robot_model_loader/robot_model_loader.h>
#include <moveit/profiler/profiler.h>
#include <tf2/LinearMath/Quaternion.h>
#include <ros/package.h>

#include <boost/math/constants/constants.hpp>

static const std::string ROBOT_DESCRIPTION = "robot_description";

moveit_msgs::Constraints getConstraints(
const std::string &name, const tf2::Quaternion &orientation, double x, double y, double z
)
{
  //tf2::Quaternion orientation;
  //orientation.setRPY(-boost::math::constants::pi<double>() / 2.0, 0, 0);

  moveit_msgs::OrientationConstraint ocm;
  ocm.link_name = "tool0_tip";
  ocm.header.frame_id = "borunte_stand_link";
  ocm.orientation.x = orientation.x();
  ocm.orientation.y = orientation.y();
  ocm.orientation.z = orientation.z();
  ocm.orientation.w = orientation.w();
  ocm.absolute_x_axis_tolerance = x;
  ocm.absolute_y_axis_tolerance = y;
  ocm.absolute_z_axis_tolerance = z;
  ocm.weight = 1.0;
  moveit_msgs::Constraints cmsg;
  cmsg.orientation_constraints.resize(1, ocm);
  cmsg.name = ocm.link_name + name;
  return cmsg;
}

void computeDB(const robot_model::RobotModelPtr &robot_model,
           unsigned int ns, unsigned int ne)
{
  planning_scene::PlanningScenePtr ps(new planning_scene::PlanningScene(robot_model));
  ompl_interface::OMPLInterface ompl_interface(robot_model);
  ompl_interface::ConstraintApproximationConstructionOptions opt;
  opt.state_space_parameterization = "PoseModel";
  opt.samples = ns;
  opt.edges_per_sample = ne;
  opt.explicit_motions = true;
  opt.max_edge_length = 0.2;
  opt.explicit_points_resolution = 0.05;
  opt.max_explicit_points = 10;

  moveit_msgs::Constraints c = getConstraints(
    ":side_360_45",
    tf2::Quaternion(-0.5, -0.5, 0.5, 0.5),
    boost::math::constants::pi<double>() / 4.0,
    2 * boost::math::constants::pi<double>(),
    boost::math::constants::pi<double>() / 4.0
  );
  ompl_interface.getConstraintsLibrary().addConstraintApproximation(c, "manipulator", ps, opt);
  c = getConstraints(
    ":side_360_22.5",
    tf2::Quaternion(-0.5, -0.5, 0.5, 0.5),
    boost::math::constants::pi<double>() / 8.0,
    2 * boost::math::constants::pi<double>(),
    boost::math::constants::pi<double>() / 8.0
  );
  ompl_interface.getConstraintsLibrary().addConstraintApproximation(c, "manipulator", ps, opt);
  c = getConstraints(
    ":side_360_11.25",
    tf2::Quaternion(-0.5, -0.5, 0.5, 0.5),
    boost::math::constants::pi<double>() / 16.0,
    2 * boost::math::constants::pi<double>(),
    boost::math::constants::pi<double>() / 16.0
  );
  ompl_interface.getConstraintsLibrary().addConstraintApproximation(c, "manipulator", ps, opt);
  const std::string path = ros::package::getPath("borunte_moveit_config") + "/config/constraints_approximation_database";
  ompl_interface.getConstraintsLibrary().saveConstraintApproximations(path);
  ROS_INFO("Done");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "construct_ompl_state_database", ros::init_options::AnonymousName);

  ros::AsyncSpinner spinner(1);
  spinner.start();

  unsigned int nstates = 1000;
  unsigned int nedges = 0;

  if (argc > 1)
    try
    {
      nstates = boost::lexical_cast<unsigned int>(argv[1]);
    }
    catch(...)
    {
    }

  if (argc > 2)
    try
    {
      nedges = boost::lexical_cast<unsigned int>(argv[2]);
    }
    catch(...)
    {
    }

  robot_model_loader::RobotModelLoader rml(ROBOT_DESCRIPTION);
  computeDB(rml.getModel(), nstates, nedges);

  ros::shutdown();
  return 0;
}
