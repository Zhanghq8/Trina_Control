#!/usr/bin/env python

import rospy
import roslib
import time
from reflex_msgs.msg import Command
import sys
import os
import random
import numpy as np



class Hand_control():

	def __init__(self):
		self.hand_pub = rospy.Publisher("/right_hand/command", Command, queue_size=10)

	#control the hand with velocity and position
	def hand_open(self):
		hand = Command()
		hand.pose.f1 = 0.0
		hand.pose.f2 = 0.0
		hand.pose.f3 = 0.0
		hand.pose.preshape = 0.0
		hand.velocity.f1 = 2.0
		hand.velocity.f2 = 2.0
		hand.velocity.f3 = 2.0
		hand.velocity.preshape = 2.0
		print "Opening hand..."
		rospy.loginfo(hand)
		time.sleep(2.0)
		self.hand_pub.publish(hand)
		print "Done..."

	def hand_close(self):
		hand = Command()
		hand.pose.f1 = 2.2
		hand.pose.f2 = 2.2
		hand.pose.f3 = 2.2
		hand.pose.preshape = 0.0
		hand.velocity.f1 = 2.0
		hand.velocity.f2 = 2.0
		hand.velocity.f3 = 2.0
		hand.velocity.preshape = 2.0
		print "Closing hand..."
		rospy.loginfo(hand)
		time.sleep(2.0)
		self.hand_pub.publish(hand)
		print "Done..."

	def hand_control(self, _f1, _f2, _f3, _v):
		hand = Command()
		hand.pose.f1 = _f1
		hand.pose.f2 = _f2
		hand.pose.f3 = _f3
		hand.pose.preshape = 0.0
		hand.velocity.f1 = _v
		hand.velocity.f2 = _v
		hand.velocity.f3 = _v
		hand.velocity.preshape = 2.0
		print "Grasping..."
		time.sleep(2.0)
		rospy.loginfo(hand)
		self.hand_pub.publish(hand)
		print "Done..."

	# def hand_shape_set(self, shape_angle):
	# 	hand = Command()
	# 	hand.pose.preshape = shaple_angle

	#hand_control demo
	def hand_demo(self):
		pass


def main(args): 
    rospy.init_node('Hand_Control', anonymous=True)
    hand = Hand_control()
    print 'Ready to control the hand...'	
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print ('Shutting down the hand...')

if __name__ == '__main__':
    main(sys.argv)
