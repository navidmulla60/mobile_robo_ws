#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from pynput import keyboard
def driver():
    pub = rospy.Publisher('driver', String,queue_size=5)
    rospy.init_node('driver')
    while not rospy.is_shutdown():

	with keyboard.Events() as events:
    
	    event = events.get()
	    if event is None:
	        print('You did not press a key within one second')
	    else:
		a=str(event.key)
		b="u\'w\'"
		c="u\'s\'"
		d="u\'a\'"
		e="u\'d\'"
	        if a == b :
		       	msg = "Forwards"
	        	rospy.loginfo(msg)
        		pub.publish(String(msg))
        		rospy.sleep(0.1)
		elif a == c :
			msg = "Backward"
	        	rospy.loginfo(msg)
        		pub.publish(String(msg))
        		rospy.sleep(0.1)
		elif a == d :
			msg = "Left"
	        	rospy.loginfo(msg)
        		pub.publish(String(msg))
        		rospy.sleep(0.1)
		elif a == e :
			msg = "Right"
	        	rospy.loginfo(msg)
        		pub.publish(String(msg))
        		rospy.sleep(0.1)

		else :
			msg = "Stop"
	        	rospy.loginfo(msg)
        		pub.publish(String(msg))
        		rospy.sleep(0.1)
			
# The event listener will be running in this block

	
if __name__ == '__main__':
    try:
        driver()
    except rospy.ROSInterruptException: pas
