#!/usr/bin/env python

import baxter_interface
import numpy as np
import rospy
import sys, time, os

class arm_control:

    def __init__(self):
        self.limb1 = baxter_interface.Limb('right')
        self.limb2 = baxter_interface.Limb('left')
        
    
    def reset_botharm(self):
        right_angles = {'right_s0': -0.7815632114276183, 'right_s1': 0.2519563444101792, 'right_w0': 1.4177817432030937, 'right_w1': 0.04026699568199211, 'right_w2': 0.1177330254702055, 'right_e0': -0.16528642989465334, 'right_e1': 1.2448254093690132}
        left_angles = {'right_s0': 0.5234709438658974, 'right_s1': 0.04908738521233324, 'right_w0': 1.2072428800658206, 'right_w1': 0.20862138715241627, 'right_w2': 0.5437961893053792, 'right_e0': -0.04180097646987752, 'right_e1': 1.5247769031581013,}
        self.limb1.move_to_joint_positions(right_angles, timeout=2.5)
        self.limb2.move_to_joint_positions(left_angles, timeout=2.5)

    def move_rightarm(self):
        move_angle = {'right_s0': -1.4442429117941171, 'right_s1': 0.2519563444101792, 'right_w0': 1.2570972556720965, 'right_w1': 0.6197282383057071, 'right_w2': 1.750272078977257, 'right_e0': -0.5530000740326917, 'right_e1': -0.0502378708032473}
        self.limb1.move_to_joint_positions(move_angle, timeout=2.5)

    def move_leftarm(self):
        pass
        # self.limb2.move_to_joint_positions(self.safe_angle, timeout=2.5)

def main():
    rospy.init_node("armmove", anonymous=True)
    move_arm = arm_control()
    # move_arm.moveright_arm()
    # move_arm.moveleft_arm()
    move_arm.reset_botharm()

if __name__ == '__main__':
    main()
