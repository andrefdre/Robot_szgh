#!/usr/bin/env python3
from math import sin 
from math import cos
import math


def main():
    pi=math.pi
    l1=0.2645
    l2x=0.21938
    l2z=0.332
    l3y=0.06500000000000014
    l4z=1.1
    l5x=0.97509
    l6x=0.1718
    l7z=0.18957

    theta2=0
    theta3=0
    theta5=0
    theta6=0
    # k1=cos(theta2)*cos(theta3)*cos(theta4)-cos(theta2)*sin(theta3)*sin(theta4)
    # k2=sin(theta2)*cos(theta3)*cos(theta4)-sin(theta2)*sin(theta3)*sin(theta4)
    # k3=cos(theta2)*cos(theta3)*sin(theta4)+cos(theta2)*sin(theta3)*cos(theta4)
    # k4=sin(theta2)*cos(theta3)*sin(theta4)+sin(theta2)*sin(theta3)*cos(theta4)
    # x = l4x*k1-l4z*k3+l2x*cos(theta2)-l3y*sin(theta2)+l3x*cos(theta2)*cos(theta3)
    # y = l4x*k2-l4z*k4+l2x*sin(theta2)+l3y*cos(theta2)+l3x*sin(theta2)*cos(theta3)
    # z = l1+l2z+l4z*cos(theta3+theta4)+l4x*sin(theta3+theta4)+l3x*sin(theta3)
    x=(l5x*cos(theta3 - theta2 + theta5))/2 + (l6x*cos(theta2 + theta3 + theta5 + theta6))/2 + (l7z*sin(theta2 + theta3 + theta5 + theta6))/2 - (l4z*sin(theta2 + theta3))/2 + l2x*cos(theta2) - l3y*sin(theta2) + (l6x*cos(theta3 - theta2 + theta5 + theta6))/2 + (l7z*sin(theta3 - theta2 + theta5 + theta6))/2 + (l4z*sin(theta2 - theta3))/2 + (l5x*cos(theta2 + theta3 + theta5))/2
    y=(l6x*sin(theta2 + theta3 + theta5 + theta6))/2 - (l7z*cos(theta2 + theta3 + theta5 + theta6))/2 - (l5x*sin(theta3 - theta2 + theta5))/2 + (l4z*cos(theta2 + theta3))/2 + l3y*cos(theta2) + l2x*sin(theta2) + (l7z*cos(theta3 - theta2 + theta5 + theta6))/2 - (l6x*sin(theta3 - theta2 + theta5 + theta6))/2 - (l4z*cos(theta2 - theta3))/2 + (l5x*sin(theta2 + theta3 + theta5))/2
    z=l1 + l2z + l5x*sin(theta3 + theta5) + l4z*cos(theta3) - l7z*cos(theta3 + theta5 + theta6) + l6x*sin(theta3 + theta5 + theta6)
    print(x,y,z)

if __name__ == '__main__':
    main()