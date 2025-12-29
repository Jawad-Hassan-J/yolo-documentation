from ultralytics import YOLO
from dotenv import load_dotenv
import os

load_dotenv()

model_path = os.getenv("YOLO_MODEL_PATH")

model = YOLO(model_path)


model.predict(
    source=0,
    show=True,
    conf=0.5
)