#!/usr/bin/env python3
from math import sin 
from math import cos
import math
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink


def main():

    my_chain = Chain.from_urdf_file("../urdf/robot.urdf")
    ikResults = my_chain.inverse_kinematics( target_position=[2, 2, 2],  target_orientation = [1, 1, -1], orientation_mode="Y")

    print(ikResults)

if __name__ == '__main__':
    main()