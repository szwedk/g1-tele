import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class G1ROS2Controller(Node):
    def __init__(self):
        super().__init__('g1_arm_controller')
        self.publisher = self.create_publisher(JointState, '/g1_arm_controller/command', 10)
        self.joint_names = [
            'shoulder_pitch', 'elbow',
            'wrist_pitch', 'wrist_roll',
            'wrist_yaw', 'gripper'  # adjust names if needed
        ]
        self.get_logger().info("ROS2 G1 controller initialized")

    def send_joint_angles(self, joint_angles):
        msg = JointState()
        msg.name = self.joint_names
        msg.position = joint_angles
        self.publisher.publish(msg)
        self.get_logger().info(f"Published joint angles: {['{:.2f}'.format(a) for a in joint_angles]}")

def start_ros2_controller(joint_angle_callback):
    rclpy.init()
    node = G1ROS2Controller()
    try:
        while rclpy.ok():
            angles = joint_angle_callback()
            if angles:
                node.send_joint_angles(angles)
            rclpy.spin_once(node, timeout_sec=0.05)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()