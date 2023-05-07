#!/usr/bin/env python3
import random
import rospy
from std_msgs.msg import Int16



def publisher_test():
    pub = rospy.Publisher('tester', Int16, queue_size=1)
    rospy.init_node('unit_tests', anonymous=False)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        random_int = random.randint(0, 100)
        rospy.loginfo(random_int)
        pub.publish(random_int)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher_test()
    except rospy.ROSInterruptException:
        pass