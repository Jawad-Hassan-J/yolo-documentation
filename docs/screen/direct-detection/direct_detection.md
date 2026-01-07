```python 
from ultralytics import YOLO
from dotenv import load_dotenv
import os

import mss
import cv2
import numpy as np
```
**mss:** fast capture library
**cv2:** deal with pictures, draw, show, convert colors and others
**numpy:** represent picture as a matrix (pixels)

```python
load_dotenv()
model_path = os.getenv("YOLO_MODEL_PATH")
model = YOLO(model_path)

```
#picture 

```python
with mss.mss() as sct:
    monitor = sct.monitors[1]
```
**mss.mss():** is a function to start environment to capture
**sct.monitors[1]:** select monitor index, an example if you have multiple monitors [1] represent first monitor, [2] second ..., while [0] is all monitor in one picture 

```python
        screenshot = sct.grab(monitor)

        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) 

        results = model(frame, conf=0.4)
```
**sct.grab(monitor):** capture screen from GPU and return mss object [mss function](../../reference/mss_grab_function.md)
**np.array(screenshot):** convert picture from current type into Numpy Array (matrix)  
**cv2.cvtColor(frame):** convert frame form ARGB into RGB, because YOLO expect RGB frame
**model(frame, conf):** 


```python

        annotated_frame = results[0].plot()
```
**results[0].plot():**
```python
cv2.imshow("YOLO", annotated_frame)
```
**:**


```python
if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
```

