#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


def cmd_vel_callback(self, twist):
    linear_x = twist.linear.x


def driver():
    rospy.init_node('red_rover_driver', anonymous=True)

    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)
    velocity_publish = rospy.Publisher('velocity/setpoint', Float64, queue_size=1)
    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    try:
        driver()
    except rospy.ROSInterruptException:
        pass