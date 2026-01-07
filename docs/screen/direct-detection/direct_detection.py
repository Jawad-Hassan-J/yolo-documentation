from ultralytics import YOLO
from dotenv import load_dotenv
import os

import mss
import cv2
import numpy as np

load_dotenv()
model_path = os.getenv("YOLO_MODEL_PATH")
model = YOLO(model_path)


with mss.mss() as sct:
    monitor = sct.monitors[1]

    while True:
        screenshot = sct.grab(monitor)

        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) 

        results = model(frame, conf=0.4)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLO", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
    