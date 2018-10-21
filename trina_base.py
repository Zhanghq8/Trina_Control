#!/usr/bin/env python

import rospy
import roslib
from geometry_msgs.msg import Twist
import sys
import os
import random
import numpy as np


class base_control():

	def __init__(self):
		self.base_control = rospy.Publisher("/amp_wpi/twist_command", Twist, queue_size=10)

	#control the base with velocity
	def base_forward_v(self):
		pass

	def base_backward_v(self):
		pass

	def base_2_left_v(self):
		pass

	def base_2_right_v(self):
		pass

	def base_rotate_v(self):
		pass


	#control the bse with position
	def base_forward_p(self):
		pass

	def base_backward_p(self):
		pass

	def base_2_left_p(self):
		pass

	def base_2_right_p(self):
		pass

	def base_rotate_p(self):
		pass

	#base_control demo
	def base_demo(self):
		pass


def main(args): 
    rospy.init_node('Base_Control', anonymous=True)
    base_pub = base_control()
    print 'Ready to control the base...'	
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ('Shutting down the base...')

if __name__ == '__main__':
    main(sys.argv)


        # base = Twist()
        # angular_speed = -0.2*PI/180
        # relative_angle = PI/2
        # base.linear.x = 0
        # base.linear.y = 0
        # base.linear.z = 0
        # base.angular.x = 0
        # base.angular.y = 0
        # base.angular.z = angular_speed

        # t0 = rospy.Time.now().to_sec()