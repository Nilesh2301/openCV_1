# cv2.VideoWriter(filename, codec, fps, frame_size)
# codec = compression format, fps = frames per second, frame_size = (w, h)

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*"XVID")
recorder = cv2.VideoWriter("my_video.avi", codec, 60, (frame_width, frame_height))

while True:
    success, image = camera.read()
    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recording Live", image)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
