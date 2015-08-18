#!/usr/bin/env python

# set up parameters that we care about
PACKAGE = 'jsk_pcl_ros'

try:
    import imp
    imp.find_module(PACKAGE)
    from dynamic_reconfigure.parameter_generator_catkin import *;
except:
    import roslib; roslib.load_manifest(PACKAGE)
    from dynamic_reconfigure.parameter_generator import *;
gen = ParameterGenerator ()

gen.add("init_local_position_z_min", double_t, 0, "", 0.0, 0.0, 1.0)
gen.add("init_local_position_z_max", double_t, 0, "", 1.0, 0.0, 1.0)
gen.add("use_init_world_position_z_model", bool_t, 0, "", False)
gen.add("init_local_orientation_roll_variance", double_t, 0, "", 0.005, 0.0, 1.0)
gen.add("init_local_orientation_pitch_variance", double_t, 0, "", 0.005, 0.0, 1.0)
gen.add("init_local_orientation_yaw_mean", double_t, 0, "", 0.0, 0.0, 1.0)
gen.add("init_local_orientation_yaw_variance", double_t, 0, "", 0.01, 0.0, 1.0)
gen.add("init_dx_mean", double_t, 0, "", 0.1, 0.0, 1.0)
gen.add("init_dx_variance", double_t, 0, "", 0.001, 0.0, 1.0)
gen.add("init_dy_mean", double_t, 0, "", 0.1, 0.0, 1.0)
gen.add("init_dy_variance", double_t, 0, "", 0.001, 0.0, 1.0)
gen.add("init_dz_mean", double_t, 0, "", 0.1, 0.0, 1.0)
gen.add("init_dz_variance", double_t, 0, "", 0.001, 0.0, 1.0)
gen.add("particle_num", int_t, 0, "", 1000, 0, 1000000)
gen.add("step_x_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_y_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_z_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_roll_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_pitch_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_yaw_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_dx_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_dy_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("step_dz_variance", double_t, 0, "", 0.0001, 0.00000001, 1.0)
gen.add("use_range_likelihood", bool_t, 0, "", False)
gen.add("range_likelihood_local_min_z", double_t, 0, "", 0.0, 0.0, 1.0)
gen.add("range_likelihood_local_max_z", double_t, 0, "", 0.0, 0.0, 1.0)
gen.add("use_occlusion_likelihood", bool_t, 0, "", False)
gen.add("min_inliers", int_t, 0, "", 10, 0, 1000)
gen.add("outlier_distance", double_t, 0, "", 0.1, 0.0, 1.0)
