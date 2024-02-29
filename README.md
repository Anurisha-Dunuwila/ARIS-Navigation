# ARIS 1.0 Navigation

ARIS 1.0 is a multitasking medical service robot specifically designed for conducting virtual ward round sessions. The robot consists of a 3-wheeled omni-directional mobile platform, and the navigation was carried by utilizing a single sensor, i.e., 2D RP Lidar and ROS Navigation stack. In the mapping phase, the robot was controlled manually using [teleop_keyboard_omni3](https://github.com/YugAjmera/teleop_keyboard_omni3/tree/master) and the hector_slam was used to generate the map. In the navigation phase, AMCL package was used to maintain map-odom transform, while hector_slam again was used to maintain odom-base_link transform. Move_base package was used to navigate the robot in its surroundings. To avoid unnecessary holonomic motion near the goal [movebase_to_manual.py](https://github.com/Anurisha-Dunuwila/ARIS-Navigation/blob/master/src/aris_navigation/movebase_to_manual.py) was executed by passing the move_base package. 

Introduction: [Youtube Video](https://youtu.be/OCDFhqT4-_A)

## Preview

[![](https://markdown-videos-api.jorgenkh.no/youtube/s0P_3uAQFFg)](https://youtu.be/s0P_3uAQFFg)



