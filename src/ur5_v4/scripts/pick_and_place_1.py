#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from std_srvs.srv import Empty
from std_msgs.msg import String

def open_gripper():
    # gripper_pub.publish('open')
    rospy.sleep(1)

def close_gripper():
    # gripper_pub.publish('close')
     rospy.sleep(1)

def go_to_pose(pose_goal):
    move_group.set_pose_target(pose_goal)
    success = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    return success

def main():
    rospy.init_node('ur5_pick_and_place', anonymous=True)

    global move_group 
    # , gripper_pub
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    move_group = moveit_commander.MoveGroupCommander("manipulator")
    # gripper_pub = rospy.Publisher('/robotiq_85_gripper/command', String, queue_size=10)

    rospy.sleep(2)

    # Posición inicial (home)
    home_pose = move_group.get_current_pose().pose
    home_pose.position.x = 0.4
    home_pose.position.y = 0
    home_pose.position.z = 1.1

    # Posición sobre el cubo1
    pick_pose = geometry_msgs.msg.Pose()
    pick_pose.orientation.w = 1.0
    pick_pose.position.x = 0.30
    pick_pose.position.y = 0.50
    pick_pose.position.z = 1.15  # sobre el cubo

    # Posición para dejar el cubo
    place_pose = geometry_msgs.msg.Pose()
    place_pose.orientation.w = 1.0
    place_pose.position.x = -0.50
    place_pose.position.y = 0
    place_pose.position.z = 1.15  # sobre el otro sitio

    # Secuencia
    open_gripper()
    go_to_pose(home_pose)
    go_to_pose(pick_pose)
    pick_pose.position.z = 1.04  # bajar al cubo
    go_to_pose(pick_pose)
    close_gripper()
    pick_pose.position.z = 1.15  # subir
    go_to_pose(pick_pose)
    go_to_pose(place_pose)
    place_pose.position.z = 1.04  # bajar para soltar
    go_to_pose(place_pose)
    open_gripper()
    place_pose.position.z = 1.15  # subir de nuevo
    go_to_pose(place_pose)
    go_to_pose(home_pose)

    rospy.loginfo("Pick and place terminado")
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
