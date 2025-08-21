

# 🤖 EmKa G1 Teleop: Human-to-Robot Arm Control via Pose Tracking

A personal robotics project by Kamil Szwed enabling intuitive, real-time control of the Unitree G1 humanoid robot using your own upper-body movements. It uses **MediaPipe Pose** to interpret webcam input and translates it into robot joint commands via **Unitree SDK** or **ROS 2**.

---

## 🔧 Project Overview

```
g1_teleop/
├── main.py                         # Launches tracking and control loop
├── config/
│   └── joint_limits.yaml           # Joint range safety configuration
├── controllers/
│   ├── sdk_controller.py           # Unitree Python SDK interface
│   └── ros2_controller.py          # ROS 2 interface (optional)
├── tracking/
│   └── pose_tracker.py             # MediaPipe Pose landmark extractor
├── utils/
│   └── joint_mapping.py            # Converts human pose to G1 joint commands
├── simulation/
│   └── sim_overlay.py              # Simulated visual feedback of movement
├── README.md                       # This documentation
└── requirements.txt                # Python dependencies
```

---

## ✅ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/szwedk/g1-tele.git && cd g1-tele
```

### 2. Create virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Set environment variables
```bash
cp .env.example .env
```

---

## 🧪 Run Visual Simulator

Try the full arm simulation before testing on real hardware:

```bash
python -m simulation.sim_overlay
```

---

## 🤝 Real-Time Robot Control

Ensure your G1 is:
- Powered on and in PC control mode
- Reachable at the IP in `main.py`

Then launch:

```bash
python main.py
```

---

## ⚙️ Customization Options

- Update joint safety thresholds in `config/joint_limits.yaml`
- Fine-tune pose-to-joint mapping in `utils/joint_mapping.py`

---

## 🧩 Dependencies

See `requirements.txt` for the full list of Python packages.

---

## 🧠 About

This is a personal side project developed at [RoboStore](https://www.robostore.com), designed to push forward intuitive human-robot interaction in real-time.

Built with 💡 by [@szwedk](https://github.com/szwedk)