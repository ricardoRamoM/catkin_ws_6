#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import tf
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_gripper(position, duration=2.0):
    pub = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=10)
    rospy.sleep(1)
    traj = JointTrajectory()
    traj.joint_names = ['robotiq_85_left_knuckle_joint']
    point = JointTrajectoryPoint()
    point.positions = [position]
    point.time_from_start = rospy.Duration(duration)
    traj.points.append(point)
    pub.publish(traj)
    rospy.sleep(duration + 1)

def pick_and_place(arm_group, cube_pos, box_pos, above_offset=0.1):
    # Calcular cuaternión de orientación fija (vertical hacia abajo)
    quaternion = tf.transformations.quaternion_from_euler(-1.57, 0.0, 0.0)

    # 1. Ir arriba del cubo (movimiento tipo joint)
    arm_group.set_joint_value_target(arm_group.get_current_joint_values())  # reset targets
    arm_group.set_position_target([cube_pos[0], cube_pos[1], cube_pos[2] + above_offset])
    arm_group.go(wait=True)

    # 2. Bajar en línea recta
    pose = geometry_msgs.msg.Pose()
    pose.position.x = cube_pos[0]
    pose.position.y = cube_pos[1]
    pose.position.z = cube_pos[2]
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    arm_group.set_pose_target(pose)
    arm_group.go(wait=True)

    # 3. Cerrar gripper
    move_gripper(0.4)

    # 4. Subir en línea recta
    pose.position.z += above_offset
    arm_group.set_pose_target(pose)
    arm_group.go(wait=True)

    # 5. Ir arriba de la caja (movimiento tipo joint)
    arm_group.set_joint_value_target(arm_group.get_current_joint_values())  # reset
    arm_group.set_position_target([box_pos[0], box_pos[1], box_pos[2] + above_offset])
    arm_group.go(wait=True)

    # 6. Bajar en línea recta
    pose.position.x = box_pos[0]
    pose.position.y = box_pos[1]
    pose.position.z = box_pos[2]
    arm_group.set_pose_target(pose)
    arm_group.go(wait=True)

    # 7. Abrir gripper
    move_gripper(0.0)

    # 8. Subir en línea recta
    pose.position.z += above_offset
    arm_group.set_pose_target(pose)
    arm_group.go(wait=True)

if __name__ == '__main__':
    try:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('pick_and_place_node', anonymous=True)
        arm_group = moveit_commander.MoveGroupCommander("manipulator")
        arm_group.set_planner_id("RRTConnectkConfigDefault")
        arm_group.set_planning_time(10)

        # Posición inicial
        arm_group.set_named_target("home")
        arm_group.go(wait=True)

        # Coordenadas de cubos (lado derecho)
        cubes = [
            [0.85, 0.45, 1.001],
            [0.85, 0.55, 1.001],
            [0.85, 0.65, 1.001],
            [0.85, 0.75, 1.001]
        ]

        # Coordenadas de cajas (lado izquierdo)
        boxes = [
            [0.5, -0.4, 1.001],  # Caja 1
            [0.5, -0.4, 1.001],  # Caja 1
            [0.5, -0.6, 1.001],  # Caja 2
            [0.5, -0.6, 1.001]   # Caja 2
        ]

        for i in range(4):
            pick_and_place(arm_group, cubes[i], boxes[i])

        # Regresar a home
        arm_group.set_named_target("home")
        arm_group.go(wait=True)

    except rospy.ROSInterruptException:
        pass