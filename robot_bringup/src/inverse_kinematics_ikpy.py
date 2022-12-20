#!/usr/bin/env python3
from math import sin 
from math import cos
import math
import os
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import rospkg
import numpy as np
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D


def main():
    rospack = rospkg.RosPack()
    
    my_chain = Chain.from_urdf_file(rospack.get_path('robot_bringup')+"/urdf/robot.urdf", base_elements=["base_link","joint1","link1","joint2","link2","joint3","link3","joint4_artificial","link4_artificial","joint4","link4","joint5","link5"])
    ikResults = my_chain.inverse_kinematics( target_position=[2, 2, 2],  target_orientation = [1, 1, -1], orientation_mode="Z")

    # The Tiago robot has multiple motors, each identified by their names below.
    # Make sure to use a parts list specific to your robot's controllable joints
    part_names = ("joint1", "joint2", "joint3", "joint5")

    for link_id in range(len(my_chain.links)):

        # This is the actual link object
        link = my_chain.links[link_id]
        
        # I've disabled "torso_lift_joint" manually as it can cause
        # the TIAGO to become unstable.
        if link.name not in part_names or  link.name =="torso_lift_joint":
            print("Disabling {}".format(link.name))
            my_chain.active_links_mask[link_id] = False

    print(my_chain.forward_kinematics([0] * 7))
    

    # Initialize the arm motors and encoders.
    motors = []
    for link in my_chain.links:
        if link.name in part_names and link.name != "torso_lift_joint":
            motor = robot.getDevice(link.name)

            # Make sure to account for any motors that
            # require a different maximum velocity!
            if link.name == "torso_lift_joint":
                motor.setVelocity(0.07)
            else:
                motor.setVelocity(1)
                
            position_sensor = motor.getPositionSensor()
            position_sensor.enable(timestep)
            motors.append(motor)

    print(np.round(ikResults,2))

if __name__ == '__main__':
    main()