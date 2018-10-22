#!/usr/bin/env python

import rospy
import roslib
from geometry_msgs.msg import Twist
import sys
import os
import random
import numpy as np


class Base_control():

	def __init__(self):
		self.base_pub = rospy.Publisher("/amp_wpi/twist_command", Twist, queue_size=10)

	#control the bse with position
	def base_x(self, v, t):
		base = Twist()
		base.linear.x = v
		t0 = rospy.Time.now().to_sec()
		time = t
		while rospy.Time.now().to_sec() - t0 < t:
			print "Moving along x_axis..."
			rospy.loginfo(base)
			self.base_pub.publish(base)
		print "Done..."


	def base_y(self, v, t):
		base = Twist()
		base.linear.y = v
		t0 = rospy.Time.now().to_sec()
		time = t
		while rospy.Time.now().to_sec() - t0 < t:
			print "Moving along y_axis..."
			rospy.loginfo(base)
			self.base_pub.publish(base)
		print "Done..."
	def base_rotate(self, v, t):
		base = Twist()
		base.angular.z = v
		t0 = rospy.Time.now().to_sec()
		time = t
		while rospy.Time.now().to_sec() - t0 < t:
			print "Rotating..."
			rospy.loginfo(base)
			self.base_pub.publish(base)
		print "Done..."

	#base_control demo
	def base_demo(self):
		pass


def main(args): 
    rospy.init_node('Base_Control', anonymous=True)
    base = Base_control()
    print 'Ready to control the base...'	
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ('Shutting down the base...')

if __name__ == '__main__':
    main(sys.argv)  
