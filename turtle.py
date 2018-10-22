#!/usr/bin/env python

import rospy
import roslib
from geometry_msgs.msg import Twist
import sys
import os
import random
import numpy as np
"""
# def turtle():
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rospy.init_node('turtle', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown():
t0 = rospy.Time.now().to_sec()
turtle_pub = Twist()
turtle_pub.linear.x= 0.2
turtle_pub.linear.y= 0.2
turtle_pub.linear.z= 0.2
turtle_pub.angular.x= 0.2
turtle_pub.angular.y= 0.2
turtle_pub.angular.z= 0.2
t = 5
while rospy.Time.now().to_sec() - t0 < t:
	print "start..."
	rospy.loginfo(turtle_pub)
	pub.publish(turtle_pub)
"""

class turtle_control():

	def __init__(self):
		self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

	def turtle_move(self):
		turtle_pub = Twist()
		turtle_pub.linear.x= 0.2
		turtle_pub.linear.y= 0.2
		turtle_pub.linear.z= 0.2
		turtle_pub.angular.x= 0.2
		turtle_pub.angular.y= 0.2
		turtle_pub.angular.z= 0.2
		t0 = rospy.Time.now().to_sec()
		t = 5
		while rospy.Time.now().to_sec() - t0 < t:
			print "start..."
			rospy.loginfo(turtle_pub)
			self.pub.publish(turtle_pub)
		print "done..."

def main(args): 
    rospy.init_node('Turtle', anonymous=True)
    numpub = turtle_control()	
    try:
		rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
