#!/usr/bin/env python3.6

import rospy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config

Config.set( "graphics",'resizable',False)

from geometry_msgs.msg import Twist

# Config.set('kivy', 'keyboard_mode', 'systemandmulti')

class myKivyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen=Builder.load_file('/home/navid/personal_projects/mobile_robo_ws/src/gui/config/ros_gui.kv')
    
    def build(self):
        return self.screen

    def right_move(self,*args):
        self.rotate.linear.x=0
        if ( self.rotate.angular.z>0):
            self.rotate.angular.z=-self.rotate.angular.z
        
        pub.publish(self.rotate)

    def left_move(self,*args):
        
        self.rotate.linear.x=0
        if ( self.rotate.angular.z<0):
            self.rotate.angular.z=-self.rotate.angular.z
        pub.publish(self.rotate)

    def up_move(self,*args):
        if (self.move.linear.x<0):
            self.move.linear.x=-self.move.linear.x 
        pub.publish(self.move)

    def down_move(self,*args):
        # print(self.move.linear.x)
        if (self.move.linear.x>0):
            self.move.linear.x=-self.move.linear.x
        print(self.move.linear.x)
        pub.publish(self.move)
        
    def stop_move(self,*args):
        move=Twist()
        move.linear.x=0
        move.linear.y=0
        move.angular.z=0
        pub.publish(move)

    def slider_linear(self, value):
        # print(value)
        self.move=Twist()
        self.move.linear.x=value
        self.move.angular.z=0
        
    def slider_angular(self, value):
        # print(value)
        self.rotate=Twist()
        self.rotate.angular.z=value

if __name__ == '__main__':
    rospy.init_node('gui_control', anonymous=True)
    pub=rospy.Publisher("/gui_cmd",Twist,queue_size=1)
    myKivyApp().run()