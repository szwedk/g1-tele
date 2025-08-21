

import math
import yaml
import os

# Load joint limits from config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'joint_limits.yaml')
with open(config_path, 'r') as f:
    joint_limits = yaml.safe_load(f)

def clamp(value, min_val, max_val):
    return max(min(value, max_val), min_val)

def map_pose_to_g1_joints(human_angles):
    """
    Maps human joint angles (degrees) to G1 joint angles (radians),
    applying normalization and joint limit clamping.
    """
    g1_angles = []

    # Shoulder pitch: map shoulder angle from ~[30–150] degrees to [-1.5, 1.5] rad
    shoulder_angle = math.radians(human_angles['right_shoulder'] - 90)
    shoulder_angle = clamp(shoulder_angle, joint_limits['shoulder_pitch']['min'], joint_limits['shoulder_pitch']['max'])
    g1_angles.append(shoulder_angle)

    # Elbow: map elbow flexion angle from ~[30–160] degrees to [-1.5, 1.5] rad
    elbow_angle = math.radians(human_angles['right_elbow'] - 90)
    elbow_angle = clamp(elbow_angle, joint_limits['elbow']['min'], joint_limits['elbow']['max'])
    g1_angles.append(elbow_angle)

    # Placeholder for wrist and additional joints
    g1_angles += [0.0] * 4

    return g1_angles