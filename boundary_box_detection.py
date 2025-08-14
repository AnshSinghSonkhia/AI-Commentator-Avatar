import cv2
import mediapipe as mp
import numpy as np
import os

# Load image
image_path = r"C:\Users\Ansh\Downloads\avatar-tech.png"
print("Trying to load image from:", os.path.abspath(image_path))
image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# Detect facial landmarks
results = face_mesh.process(rgb_image)

if results.multi_face_landmarks:
    h, w, _ = image.shape
    landmarks = results.multi_face_landmarks[0]

    # Important landmark indices (lips, cheeks, chin)
    key_indices = list(set([
        # Lips
        61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291,
        146, 91, 181, 84, 17, 314, 405, 321, 375,
        # Chin
        152, 377, 400, 378, 379, 365,
        # Cheeks
        50, 101, 205, 430
    ]))

    points = np.array([(int(landmarks.landmark[i].x * w), int(landmarks.landmark[i].y * h)) for i in key_indices])
    x_min, y_min = np.min(points, axis=0)
    x_max, y_max = np.max(points, axis=0)

    # Draw bounding box
    boxed_image = image.copy()
    cv2.rectangle(boxed_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    cv2.imshow("Lip Sync Region", boxed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Accurate Coordinates for Lip Syncing Region:")
    print(f"Top: {y_min}, Bottom: {y_max}, Left: {x_min}, Right: {x_max}")
else:
    print("No face detected.")
