#!/usr/bin/env python3
from math import sin 
from math import cos
import math


def main():
    pi=math.pi
    l1=0.2645
    l2x=0.332
    l2z=0.247
    l3x=1.1
    l3y=0.06926
    l4x=0.97283
    l4z=0.18953

    theta2=0
    theta3=1.57
    theta4=-1.57
    theta6=0
    # k1=cos(theta2)*cos(theta3)*cos(theta4)-cos(theta2)*sin(theta3)*sin(theta4)
    # k2=sin(theta2)*cos(theta3)*cos(theta4)-sin(theta2)*sin(theta3)*sin(theta4)
    # k3=cos(theta2)*cos(theta3)*sin(theta4)+cos(theta2)*sin(theta3)*cos(theta4)
    # k4=sin(theta2)*cos(theta3)*sin(theta4)+sin(theta2)*sin(theta3)*cos(theta4)
    # x = l4x*k1-l4z*k3+l2x*cos(theta2)-l3y*sin(theta2)+l3x*cos(theta2)*cos(theta3)
    # y = l4x*k2-l4z*k4+l2x*sin(theta2)+l3y*cos(theta2)+l3x*sin(theta2)*cos(theta3)
    # z = l1+l2z+l4z*cos(theta3+theta4)+l4x*sin(theta3+theta4)+l3x*sin(theta3)
    x=l4z*(cos(theta2)*cos(theta3)*sin(theta4) + cos(theta2)*cos(theta4)*sin(theta3)) - l4x*(cos(theta2)*sin(theta3)*sin(theta4) - cos(theta2)*cos(theta3)*cos(theta4)) + l2x*cos(theta2) - l3y*sin(theta2) + l3x*cos(theta2)*cos(theta3)
    y=l4z*(cos(theta3)*sin(theta2)*sin(theta4) + cos(theta4)*sin(theta2)*sin(theta3)) - l4x*(sin(theta2)*sin(theta3)*sin(theta4) - cos(theta3)*cos(theta4)*sin(theta2)) + l3y*cos(theta2) + l2x*sin(theta2) + l3x*cos(theta3)*sin(theta2)
    z=l1 + l2z - l4z*cos(theta3 + theta4) + l4x*sin(theta3 + theta4) + l3x*sin(theta3)
    print(x,y,z)

if __name__ == '__main__':
    main()