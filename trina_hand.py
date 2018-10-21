#!/usr/bin/env python

import rospy
import roslib
from reflex_msgs.msg import Command
import sys
import os
import random
import numpy as np


class hand_control():

	def __init__(self):
		self.hand_control = rospy.Publisher("/right_hand/command", Command, queue_size=10)

	#control the hand with velocity and position
	def hand_open(self, _v):
		# control_hand() = Command()
		# control_hand.pose.f1 = 0.0
		# control_hand.pose.f2 = 0.0
		# control_hand.pose.f3 = 0.0
		# control_hand.velocity.f1= 2.0
		# control_hand.velocity.f2= 2.0
		# control_hand.velocity.f3= 2.0
		pass

	def hand_close(self, _v):
		# control_hand() = Command()
		# control_hand.pose.f1 = 1.0
		# control_hand.pose.f2 = 1.0
		# control_hand.pose.f3 = 1.0
		# control_hand.velocity.f1= 2.0
		# control_hand.velocity.f2= 2.0
		# control_hand.velocity.f3= 2.0
		pass

	def hand_control(self, _f1, _f2, _f3, _v):
		# control_hand() = Command()
		# control_hand.pose.f1 = _f1
		# control_hand.pose.f2 = -f2
		# control_hand.pose.f3 = _f3
		# control_hand.velocity.f1= _v
		# control_hand.velocity.f2= _v
		# control_hand.velocity.f3= _v
		pass

	def hand_shape_set(self, shape_angle):
		# control_hand() = Command()
		# control_hand.pose.preshape = shaple_angle
		pass

	#hand_control demo
	def hand_demo(self):
		pass


def main(args): 
    rospy.init_node('Hand_Control', anonymous=True)
    hand_pub = hand_control()
    print 'Ready to control the hand...'	
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ('Shutting down the hand...')

if __name__ == '__main__':
    main(sys.argv)
