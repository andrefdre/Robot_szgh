#!/usr/bin/env python3
import rospy

import math
import tf2_ros
import tf
import geometry_msgs.msg
import turtlesim.srv
from tf.transformations import euler_from_quaternion

def main():
    rospy.init_node('listener_moon_to_venus')


    listener = tf.TransformListener()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('link5','base_link',rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        angles= euler_from_quaternion(rot)
        print ('translation: ',trans)
        angles = euler_from_quaternion(rot)
        print ('rotation: ',[(180.0/math.pi)*i for i in angles])

        rate.sleep()


if __name__ == '__main__':
    main()