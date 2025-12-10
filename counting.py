from ultralytics import YOLO
import cv2
import math
import os
import time


model = YOLO("yolov8n.pt")  # you can switch to yolov8s.pt for higher accuracy


video_path = r"c:\Users\Nilesh gupta\Downloads\2103099-uhd_3840_2160_30fps.mp4"  # change this to your downloaded traffic video file
if not os.path.exists(video_path):
    print("❌ Error: Video file not found!")
    exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error: Cannot open video file.")
    exit()


resize_width, resize_height = 900, 600
line_y = 400
offset = 15
fps = cap.get(cv2.CAP_PROP_FPS)
frame_delay = int(1000 / fps)
meters_per_pixel = 0.06 

vehicle_count = {
    "car": 0,
    "bus": 0,
    "truck": 0,
    "motorbike": 0,
    "ambulance": 0
}

track_data = {}  


fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("NileshGupta_vehicle_ambulance_output.mp4", fourcc, fps, (resize_width, resize_height))

print("🚦 Detecting vehicles, including ambulances, counting & estimating speed...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Processing complete.")
        break

    frame = cv2.resize(frame, (resize_width, resize_height))
    current_time = time.time()
    results = model(frame, stream=True)

   
    cv2.line(frame, (0, line_y), (resize_width, line_y), (0, 255, 255), 3)

    detected_ids = []
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls].lower()  

            is_ambulance = any(keyword in name for keyword in ["ambulance", "emergency"])

            if name in ["car", "bus", "truck", "motorbike"] or is_ambulance:
                if conf < 0.5:
                    continue

               
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

               
                assigned_id = None
                for vid, (px, py, pt, _, vtype) in track_data.items():
                    if math.hypot(cx - px, cy - py) < 50 and vtype == name:
                        assigned_id = vid
                        break
                if assigned_id is None:
                    assigned_id = len(track_data) + 1

                
                if assigned_id in track_data:
                    px, py, pt, _, _ = track_data[assigned_id]
                    dt = current_time - pt
                    dist = math.hypot(cx - px, cy - py)
                    speed_mps = (dist * meters_per_pixel) / dt if dt > 0 else 0
                    speed_kmph = speed_mps * 3.6
                else:
                    speed_kmph = 0

                
                vehicle_type = "ambulance" if is_ambulance else name
                track_data[assigned_id] = [cx, cy, current_time, speed_kmph, vehicle_type]
                detected_ids.append(assigned_id)

                
                color = (0, 255, 0)
                if vehicle_type == "ambulance":
                    color = (0, 0, 255) 

                # Draw box and info
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{vehicle_type} {conf:.2f}", (x1, y1 - 8),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                cv2.putText(frame, f"Speed: {speed_kmph:.1f} km/h", (x1, y2 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                
                if line_y - offset < cy < line_y + offset:
                    vehicle_count[vehicle_type] += 1

    
    to_delete = [vid for vid in track_data if vid not in detected_ids]
    for vid in to_delete:
        del track_data[vid]

   
    start_y = 40
    cv2.putText(frame, "🚘 Vehicle & Ambulance Count Dashboard", (30, start_y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    for i, (vtype, count) in enumerate(vehicle_count.items()):
        y_pos = start_y + 40 * (i + 1)
        avg_speed = 0
        speeds = [data[3] for data in track_data.values() if data[4] == vtype and data[3] > 0]
        if len(speeds) > 0:
            avg_speed = sum(speeds) / len(speeds)
        color = (255, 255, 255) if vtype != "ambulance" else (0, 0, 255)
        cv2.putText(frame, f"{vtype.capitalize()}: {count} | Avg Speed: {avg_speed:.1f} km/h",
                    (40, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.putText(frame, "Project by: Nilesh Gupta", (40, resize_height - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    out.write(frame)
    cv2.imshow("Nilesh Gupta - Vehicle & Ambulance Detection", frame)

    if cv2.waitKey(frame_delay) == 27:  # ESC key
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Output saved as: NileshGupta_vehicle_ambulance_output.mp4")
