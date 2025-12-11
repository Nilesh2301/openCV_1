import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import random

# Haar cascades
face_cascade = cv2.CascadeClassifier("FACE_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("FACE_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("FACE_detection/haarcascade_smile.xml")

# Emotion logs
log = []

# Graph setup
plt.style.use("ggplot")
fig, ax = plt.subplots()
x_vals, y_vals = [], []
emotion_to_number = {"Neutral": 0, "Happy": 1, "Angry": 2}

def update_graph(frame):
    ax.clear()
    ax.plot(x_vals[-50:], y_vals[-50:], marker="o")
    ax.set_ylim(-1, 3)
    ax.set_yticks([0,1,2])
    ax.set_yticklabels(["Neutral", "Happy", "Angry"])
    ax.set_title("Live Emotion Levels (Last 50 frames)")
    ax.set_xlabel("Frame")

ani = FuncAnimation(fig, update_graph, interval=300)

# RULE-BASED EMOTION DETECTION
def detect_emotion(eye_count, smile_count, face_ratio):
    score_angry = 0
    score_happy = 0

    # Happy score
    if smile_count > 0:
        score_happy = min(100, smile_count * 20 + random.randint(5, 25))

    # Angry score
    if eye_count > 0 and smile_count == 0:
        score_angry = int(face_ratio * 50)

    # Decide emotion
    if score_happy > 40:
        return "Happy", score_happy
    if score_angry > 40:
        return "Angry", score_angry
    return "Neutral", 20

# Glow animation variable
glow_phase = 0

cap = cv2.VideoCapture(0)
frame_index = 0

# Timeline strip (bottom of screen)
timeline = np.zeros((50, 640, 3), dtype=np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    display_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    emotion = "Neutral"
    score = 20

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 8)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)

        face_ratio = h / float(w)

        # Predict emotion + score
        emotion, score = detect_emotion(len(eyes), len(smile), face_ratio)

        # Timeline color update
        color_map = {
            "Happy": (0,255,0),
            "Angry": (0,0,255),
            "Neutral": (0,255,255)
        }
        timeline[:, frame_index % 640] = color_map[emotion]

        # Glow animation
        glow_phase += 0.2
        glow_color = (
            int(128 + 127*np.sin(glow_phase)),
            int(128 + 127*np.sin(glow_phase + 2)),
            int(128 + 127*np.sin(glow_phase + 4)),
        )

        glow = display_frame.copy()
        cv2.rectangle(glow, (x, y), (x+w, y+h), glow_color, 20)
        cv2.addWeighted(glow, 0.3, display_frame, 0.7, 0, display_frame)

        # Emotion-based visual effects
        if emotion == "Happy":
            cv2.putText(display_frame, "✨ HAPPY ✨", (x, y-10),
                        cv2.FONT_HERSHEY_DUPLEX, 0.9, (0,255,0), 3)

            # Sparkles
            for _ in range(15):
                sx = random.randint(x, x+w)
                sy = random.randint(y, y+h)
                cv2.circle(display_frame, (sx, sy), 2, (0,255,255), -1)

        elif emotion == "Angry":
            cv2.putText(display_frame, "🔥 ANGRY 🔥", (x, y-10),
                        cv2.FONT_HERSHEY_DUPLEX, 0.9, (0,0,255), 3)

            # Heatmap overlay
            heat = np.zeros_like(display_frame)
            heat[:] = (0,0,255)
            cv2.addWeighted(heat, min(0.4, score/150), display_frame, 1, 0, display_frame)

        else:
            cv2.putText(display_frame, "😐 NEUTRAL", (x, y-10),
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,0), 2)

        # Confidence meter
        cv2.rectangle(display_frame, (x, y+h+10), (x+100, y+h+30), (40,40,40), -1)
        cv2.rectangle(display_frame, (x, y+h+10), (x+score, y+h+30), (0,255,0), -1)
        cv2.putText(display_frame, f"{score}%", (x+110, y+h+27),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    # Attach timeline bar
    display_frame[-50:] = timeline

    # Logging
    timestamp = time.strftime("%H:%M:%S")
    log.append([frame_index, timestamp, emotion, score])
    x_vals.append(frame_index)
    y_vals.append(emotion_to_number[emotion])

    frame_index += 1

    cv2.imshow("Emotion Detector PRO (Pure OpenCV Edition)", display_frame)
    plt.pause(0.001)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save CSV
df = pd.DataFrame(log, columns=["Frame", "Time", "Emotion", "Score"])
df.to_csv("emotion_log.csv", index=False)
print("Saved emotion_log.csv")

cap.release()
cv2.destroyAllWindows()
plt.close()
