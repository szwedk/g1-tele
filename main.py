import argparse
from tracking.pose_tracker import PoseTracker
from controllers.sdk_controller import G1SDKController
from utils.joint_mapping import map_pose_to_g1_joints
def main():
    parser = argparse.ArgumentParser(description="G1 Upper Body Teleoperation")
    parser.add_argument("--mode", choices=["sdk", "ros"], default="sdk", help="Control mode: sdk or ros")
    args = parser.parse_args()

    print(f"[INFO] Starting G1 teleoperation in {args.mode.upper()} mode...")

    pose_tracker = PoseTracker()

    if args.mode == "sdk":
        controller = G1SDKController(ip="192.168.123.161")
        try:
            while True:
                joint_angles = pose_tracker.get_upper_body_angles()
                if joint_angles:
                    g1_angles = map_pose_to_g1_joints(joint_angles)
                    controller.send_joint_angles(g1_angles)
        except KeyboardInterrupt:
            print("\n[INFO] Teleoperation stopped.")
    elif args.mode == "ros":
        from controllers.ros2_controller import start_ros2_controller
        try:
            start_ros2_controller(lambda: map_pose_to_g1_joints(pose_tracker.get_upper_body_angles()))
        except KeyboardInterrupt:
            print("\n[INFO] ROS 2 Teleoperation stopped.")

if __name__ == "__main__":
    main()