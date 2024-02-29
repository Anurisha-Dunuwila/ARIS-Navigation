#!/usr/bin/env python

# import rospy
# from geometry_msgs.msg import Twist

# class basic_subscriber:
#     def __init__(self):
#         self.image_sub = rospy.Subscriber("/cmd_vel", Twist, self.callback)
#         print("Initializing the instance!")

#     def callback(self, twist):
#         linear_x = twist.linear.y
#         rospy.loginfo(rospy.get_caller_id() + " The linear x velocity is %f", linear_x)
#         print('Callback executed!')

# def main():
#     sub = basic_subscriber()
#     print('Currently in the main function...')
#     rospy.init_node('listener', anonymous=True)
#     rospy.spin()

# if __name__ == '__main__':
#     try:
#         main()
#     except rospy.ROSInterruptException:
#         pass

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

L = 0.3

class basic_subscriber:
    def __init__(self):
        self.image_sub = rospy.Subscriber("/cmd_vel", Twist, self.callback)
        self.publ = rospy.Publisher('vell', Float64, queue_size=1)
        self.pubb = rospy.Publisher('velb', Float64, queue_size=1)
        self.pubr = rospy.Publisher('velr', Float64, queue_size=1)
        print("Initializing the instance!")

    def callback(self, twist):

        if (0.03 <= twist.linear.x <= 0.18) or (0.03 <= twist.linear.y <= 0.18) or (0.03 <= twist.angular.z <= 0.26):
            linear_x = twist.linear.x + 0.2
            linear_y = twist.linear.y + 0.2
            angular_z = twist.angular.z + 0.2
        elif (-0.18 <= twist.linear.x <= -0.03) or (-0.18 <= twist.linear.y <= -0.03) or (-0.26 <= twist.angular.z <= -0.03):
            linear_x = twist.linear.x - 0.2
            linear_y = twist.linear.y - 0.2
            angular_z = twist.angular.z - 0.2
        else:
            linear_x = twist.linear.x
            linear_y = twist.linear.y
            angular_z = twist.angular.z


        # linear_x = twist.linear.x
        # linear_y = twist.linear.y
        # angular_z = twist.angular.z

        vell = Float64()
        velb = Float64()
        velr = Float64()

        # vell.data=-linear_y/2 - ((3**0.5)/2)*linear_x + L*angular_z

        # velb.data=linear_y + L*angular_z

        # velr.data=-linear_y/2 + ((3**0.5)/2)*linear_x + L*angular_z

        vell.data=linear_y/2 + ((3**0.5)/2)*linear_x - L*angular_z

        velb.data=-linear_y - L*angular_z

        velr.data=linear_y/2 - ((3**0.5)/2)*linear_x - L*angular_z



        
        # if linear_z!=0:
        #     velr.data = -linear_z
        #     vell.data = -linear_z
        #     velb.data = -linear_z
        # else:
        #     velr.data = -linear_x
        #     vell.data = linear_x
        #     velb.data = 0

        self.publ.publish(vell)
        self.pubb.publish(velb)
        self.pubr.publish(velr)

        #rospy.loginfo(rospy.get_caller_id() + " Published velocities: velr = %f, vell = %f, velb = %f", velr.data , vell.data, velb.data)
        #print('Callback executed!')

def main():
    sub = basic_subscriber()
    print('Currently in the main function...')
    rospy.init_node('listener', anonymous=True)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

