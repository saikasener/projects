#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Listener: Hello Şaika!")  

def listener():
    rospy.init_node('composiv_listener', anonymous=True)  
    rospy.Subscriber('composiv_topic', String, callback)  
    rospy.spin()  

if __name__ == '__main__':
    listener()
