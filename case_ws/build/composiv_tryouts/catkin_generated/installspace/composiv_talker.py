#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher_test():
    pub = rospy.Publisher('composiv_topic', String, queue_size=10)  
    rospy.init_node('composiv_talker')  
    rate = rospy.Rate(5)  

    while not rospy.is_shutdown():
        hello_str = "Talker: Hello Etaration Team!" 
        rospy.loginfo(hello_str) 
        pub.publish(hello_str)  
        rate.sleep()  



if __name__ == '__main__':
    try:
        publisher_test()
    except rospy.ROSInterruptException:
        pass
