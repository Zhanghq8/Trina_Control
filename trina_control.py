#!/usr/bin/env python
import sys
import rospy
import time
import numpy as np
import turtle
import trina_base
import trina_hand
from geometry_msgs.msg import Twist
from reflex_msgs.msg import Command

# def turtle():
#     rospy.init_node("Turtle_Experiment", disable_signals=True)
#     turtle_1 = turtle.turtle_control()
#     turtle_1.turtle_move()

def base_move():
    rospy.init_node("Base_control", disable_signals=True)
    base_1 = trina_base.Base_control()
    base_1.base_rotate(0.2, 1)

def hand_control():
    rospy.init_node("Hand_control", disable_signals=True)
    hand_1 = trina_hand.Hand_control()
    hand_1.hand_control(2, 2, 2)

def main():
	# base_move()
	hand_control()

if __name__ == '__main__':
    main()