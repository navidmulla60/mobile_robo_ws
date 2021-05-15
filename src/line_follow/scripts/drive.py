#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def driver():
    pub = rospy.Publisher('driver', String)
    rospy.init_node('driver')
    while not rospy.is_shutdown():
        str = "Forwards"
        rospy.loginfo(str)
        pub.publish(String(str))
        rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        driver()
    except rospy.ROSInterruptException: pas




