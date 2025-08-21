

import math

class G1SDKController:
    def __init__(self, ip="192.168.123.161"):
        self.ip = ip
        print(f"[SDK] Initialized G1SDKController with IP: {self.ip}")

    def send_joint_angles(self, joint_angles):
        """
        Simulates sending joint angles to the G1 arm.
        Replace with actual SDK calls if available.
        """
        print(f"[SDK] Sending joint angles (radians): {['{:.2f}'.format(a) for a in joint_angles]}")
        # TODO: Integrate actual Unitree SDK send function here.