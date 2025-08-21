


import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    ab = [a.x - b.x, a.y - b.y]
    cb = [c.x - b.x, c.y - b.y]
    dot = ab[0] * cb[0] + ab[1] * cb[1]
    norm_ab = math.hypot(ab[0], ab[1])
    norm_cb = math.hypot(cb[0], cb[1])
    if norm_ab * norm_cb == 0:
        return 0.0
    angle = math.acos(dot / (norm_ab * norm_cb))
    return math.degrees(angle)

def run_simulation_overlay():
    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose(static_image_mode=False, model_complexity=1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark

            r_shoulder = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            r_elbow = lm[mp_pose.PoseLandmark.RIGHT_ELBOW]
            r_wrist = lm[mp_pose.PoseLandmark.RIGHT_WRIST]
            r_hip = lm[mp_pose.PoseLandmark.RIGHT_HIP]

            shoulder_angle = calculate_angle(r_hip, r_shoulder, r_elbow)
            elbow_angle = calculate_angle(r_shoulder, r_elbow, r_wrist)

            cv2.putText(frame, f"Shoulder: {int(shoulder_angle)} deg", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Elbow: {int(elbow_angle)} deg", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('G1 Pose Simulation', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()