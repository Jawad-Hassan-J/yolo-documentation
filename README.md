
# yolo-documentation

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