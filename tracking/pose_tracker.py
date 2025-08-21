

import cv2
import mediapipe as mp
import math

class PoseTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.pose = mp.solutions.pose.Pose(static_image_mode=False, model_complexity=1)
        self.last_angles = None

    def _calculate_angle(self, a, b, c):
        """Calculate the angle at point b between points a and c."""
        ab = [a.x - b.x, a.y - b.y]
        cb = [c.x - b.x, c.y - b.y]
        dot = ab[0] * cb[0] + ab[1] * cb[1]
        norm_ab = math.hypot(ab[0], ab[1])
        norm_cb = math.hypot(cb[0], cb[1])
        if norm_ab * norm_cb == 0:
            return 0.0
        cos_angle = dot / (norm_ab * norm_cb)
        angle = math.acos(min(1.0, max(-1.0, cos_angle)))
        return math.degrees(angle)

    def get_upper_body_angles(self):
        success, frame = self.cap.read()
        if not success:
            return self.last_angles

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)

        if not results.pose_landmarks:
            return self.last_angles

        lm = results.pose_landmarks.landmark

        # Right arm keypoints
        right_shoulder = lm[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER]
        right_elbow = lm[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW]
        right_wrist = lm[mp.solutions.pose.PoseLandmark.RIGHT_WRIST]
        right_hip = lm[mp.solutions.pose.PoseLandmark.RIGHT_HIP]

        # Left arm keypoints
        left_shoulder = lm[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER]
        left_elbow = lm[mp.solutions.pose.PoseLandmark.LEFT_ELBOW]
        left_wrist = lm[mp.solutions.pose.PoseLandmark.LEFT_WRIST]
        left_hip = lm[mp.solutions.pose.PoseLandmark.LEFT_HIP]

        # Calculate angles
        right_shoulder_angle = self._calculate_angle(right_hip, right_shoulder, right_elbow)
        right_elbow_angle = self._calculate_angle(right_shoulder, right_elbow, right_wrist)

        left_shoulder_angle = self._calculate_angle(left_hip, left_shoulder, left_elbow)
        left_elbow_angle = self._calculate_angle(left_shoulder, left_elbow, left_wrist)

        self.last_angles = {
            "right_shoulder": right_shoulder_angle,
            "right_elbow": right_elbow_angle,
            "left_shoulder": left_shoulder_angle,
            "left_elbow": left_elbow_angle
        }

        return self.last_angles