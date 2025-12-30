from ultralytics import YOLO
import cv2
from dotenv import load_dotenv
import os

load_dotenv()
model_path = os.getenv("YOLO_MODEL_PATH")
model = YOLO(model_path)

class Config:
    def __init__(self):
        self.camera_index = 0
        self.conf_threshold = 0.5
        self.target_class = "person"
        self.show_window = True

config = Config()


cap = cv2.VideoCapture(config.camera_index)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(
        source=frame,
        conf=config.conf_threshold,
        verbose=False
    )

   
    detected = False
    for result in results:
        if result.boxes is None:
            continue

        for class_id in result.boxes.cls.tolist():
            class_name = model.names[int(class_id)]

            if class_name == config.target_class:
                detected = True

            if detected:
                print("There are a person")

            if config.show_window:
                cv2.imshow("YOLO Camera",frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

cap.release()
cv2.destroyAllWindows()