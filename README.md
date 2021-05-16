I have recenty created a repository of my work named as mobilerobot_ws

   you can see in this work I have created CAD model from scratch
   added all controller and wrote all YAML files manually
   and finally developed navigation stack for the robot.

-after that i have created line following algorithm -manually created a world with custmised line drawn on the ground floor

   also i have just implemented YOLO object recognition ( i have followed a youtube tutorial to do this... So still learning )


clone the repository and build the workspace....

there will be 8 packages... 

-Kbot_description contains all discription of robot

-kbot_simple_control use to control robot with keyboard

-navigation used for mapping and navigate robot arond the map

-line_follow used to make robot to follow line

-rviz_camera_stream is used visualization in GUI app (work in progress)

-gui package used to control the robot using user interface app

-darknet is default repository used for object recognition

-yolo_package, in this roslanch and other world file created in order to test darknet package mentioned above.

to visualise robot in rviz and in gazebo launch this file

    roslaunch kbot_description kbot_base_rviz_gazebo.launch (rviz launch file)
  
for mapping you need to this launch file 
  
    roslaunch navigation amcl.launch 
    
  -and another is 
  
      roslaunch navigation slam_gmapping.launch 
      
  once the mapping is done save the map and then, launch amcl and rviz launch file (dont launch slam_gmapping launch file )
  configure and give the end position.

for line following robot launch this file

    roslaunch line_follow course.launch
    
    rosrun line_follow controller.py   
    
   (make sure controller.py is executable.... use this command 'chmod +x controller.py')

for keyboard controlling

    roslaunch kbot_description kbot_base_rviz_gazebo.launch

    roslaunch kbot_simple_control kbot_control_teleop.launch

for yolo

    roslaunch yolo_package gazebo_rviz.launch
    
    roslaunch yolo_package yolo_v2_tiny.launch  
    
   (add some object in gazebo and  move robot around)

for gui

    roslaunch kbot_description kbot_base_rviz_gazebo.launch

    roslaunch gui gui.launch
