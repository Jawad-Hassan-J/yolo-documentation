
# yolo-documentation

## Documentation
- [Camerea](docs/camera/camera.md)


## What is YOLO
#### YOLO (You Only Look Once) is a state-of-the-art real-time object detection model that detects objects in images and videos in a single pass through a neural network. It is designed to be fast, accurate, and easy to use for real-world computer vision applications.
**Source:** Ultralytics (https://docs.ultralytics.com)

## Model Types of YOLO
| Model        | Meaning     | Speed     | Accuracy  |
| ------------ | ----------- | --------- | --------- |
| `yolov8n.pt` | Nano        | Very Fast | Low       |
| `yolov8s.pt` | Small       | Fast      | Medium    |
| `yolov8m.pt` | Medium      | Moderate  | High      |
| `yolov8l.pt` | Large       | Slow      | Very High |
| `yolov8x.pt` | Extra Large | Very Slow | Highest   |

**Source:** Ultralytics (https://docs.ultralytics.com/models/yolov8/#supported-tasks-and-modes)

## Requirements
- Python 3.9

---

## Create `.venv` for this project
```bash
py -3.9 -m venv .venv
```

---

## Activate virtual environment
```bash
. .venv/Scripts/activate
```

---

## Install dependencies
```bash
python -m pip install --upgrade pip
pip install ultralytics
pip install opencv-python
pip install numpy matplotlib pillow
pip install python-dotenv
pip install mss
```

---

## CPU
```bash
pip install torch torchvision torchaudio
```

---

## NVIDIA GPU
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Verify install (For NVIDIA GPU)
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

---

## Download model
```bash
yolo predict model=<model_name> source=0
```

### Example
```bash
yolo predict model=yolov8n.pt source=0
```

---

## Create `.env` file in project root
```bash
touch .env
```

### Inside `.env` file add:
```env
YOLO_MODEL_PATH=<your model path>
```
### Example
```env
YOLO_MODEL_PATH=./yolov8n.pt 
```

---

### Block of import we will use this alot 
```python
from ultralytics import YOLO
from dotenv import load_dotenv
import os
```
**ultralytics:** the main library for YOLO models, YOLO is class for object detection 
**dotenv,load_dotenv:** we use .env to crate a variables we dont want to share or to make code dynamic when we need to edit 
**os:** we use os to interact with operating system, and in this case we use os for getenv variables

### 
```python 
load_dotenv()
model_path = os.getenv("YOLO_MODEL_PATH")
model = YOLO(model_path)
```

**load_dotenv():** is a function used to find .env file in project start from root until find .env file
**os.getenv():** function accept variable name in .env file and take the value of this variable 
**YOLO(<modle_name>):** invoke YOLO model to use it

