#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import String
import math
from actionlib_msgs.msg import GoalID

rospy.init_node('goal_monitor')
listener = tf.TransformListener()

def goal_distance(current_pose):
    global gx,gy
    try:
    
        # listener.waitForTransform('/map', '/base_link', rospy.Time(), rospy.Duration(1.0))
        # (trans, rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        # current_pose = PoseStamped()
        
        # current_pose.pose.position.x = trans[0]
        # current_pose.pose.position.y = trans[1]
        # current_pose.pose.position.z = trans[2]
        # current_pose.pose.orientation.x = rot[0]
        # current_pose.pose.orientation.y = rot[1]
        # current_pose.pose.orientation.z = rot[2]
        # current_pose.pose.orientation.w = rot[3]

        cx=current_pose.pose.position.x 
        cy=current_pose.pose.position.y
        

        # Calculate the Euclidean distance using current_pose and goal
        # distance = math.sqrt(
        #     (current_pose.pose.position.x - goal.pose.position.x) ** 2 +
        #     (current_pose.pose.position.y - goal.pose.position.y) ** 2 +
        #     (current_pose.pose.position.z - goal.pose.position.z) ** 2
        # )

        distance = math.sqrt((cx - gx) ** 2 +(cy - gy) ** 2 )
        print(gx,gy, "\n")
        print(cx,cy,distance, "\n")
       
        
        return distance
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.logwarn("Transform lookup failed.")

def goal_reached():
    # Stop the robot when the goal is reached
    velocity_command = Twist()
    velocity_command.linear.x = 0.0
    velocity_command.angular.z = 0.0
    cmd_vel_pub.publish(velocity_command)
    rospy.loginfo("Goooooooooooooooo!")


def goal_callback(goal):
    global gx, gy
    gx=goal.pose.position.x 
    gy=goal.pose.position.y 
    while True:
        goal_sub1 = rospy.Subscriber('/amcl_pose', PoseStamped, goal_distance)
        distance = goal_distance(goal_sub1)
        if distance <= 0.01:  # Adjust the threshold as needed
            goal_reached()
        elif distance <= 1.0:
            cancel_move_base_goal()
            velocity_command = Twist()
            velocity_command.linear.x = 0.5
            velocity_command.angular.z = 0.0
            cmd_vel_pub.publish(velocity_command)
        else:
            pass



def cancel_move_base_goal():
    # Create a publisher to publish GoalID messages to /move_base/cancel
    cancel_goal_pub = rospy.Publisher('/move_base/cancel', GoalID, queue_size=1)

    # Create a GoalID message with an empty ID to cancel the current goal
    cancel_msg = GoalID()

    # Publish the GoalID message to cancel the current goal
    cancel_goal_pub.publish(cancel_msg)

    rospy.loginfo("Move Base goal canceled.")


if __name__ == '__main__':
    print("\n\n\n\n\n\n Goal monitor script is running...\n\n\n\n\n\n")
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    goal_sub = rospy.Subscriber('/move_base_simple/goal', PoseStamped, goal_callback)

    rospy.spin()


# rostopic pub /cmd_vel geometry_msgs/Twist "linear:
#   x: 0.5
#   y: 0.0
#   z: 0.0
# angular:
#   x: 0.0
#   y: 0.0
#   z: 0.3"