# Detection with action

### from the name we will make action when specific class appear, an example when you drive and use the phone the model detect your phone and you must to pay, because you break the rules.

### The idea of this section: first we will open the camera then we will take picture by picture **frame** and put each picture in the model to process by using model.**predict**(source: <your current frame>) and the model will detect of any class appear or not.
### repeat  all this process by using loop -> take picture(**frame**) -> use model to process the picture -> make action by using if statement if the class appear do this  


```python
from ultralytics import YOLO
import cv2
from dotenv import load_dotenv
import os

load_dotenv()
model_path = os.getenv("YOLO_MODEL_PATH")
model = YOLO(model_path)

```
### First section is imports and prepare the model I explain this in **Direct Detection** Folder

```python
class Config:
    def __init__(self):
        self.camera_index = 0
        self.conf_threshold = 0.5
        self.target_class = "person"
        self.show_window = True

config = Config()
```
### This powerful technique, because there are prepare configuration you can use normal Variable such camera_index = 0; target_class="person" and other but the idea here you can just type config. and the auto complete will show the available variables, also you can use dictionary for make code clear but create class is more powerful.

**camera_index:** your camera source
**conf_threshold:** the model give you class and percentage of this class, e.g(person, 50%) so we need only the threshold more than 50 to show trust classes  
**target_class:** what we need from model to focuses on, I will show you later how to know available classes.
**show_window:** to open window and show you what model see or in other words show you the **camera**

```python
cap = cv2.VideoCapture(config.camera_index)
```

**cv2.VideoCapture(video):** function accept video as a parameter to get frames for video source, in this case we open video source as a camera index


```python
while True:
    ret, frame = cap.read()
    if not ret:
        break

```
**while True:** because each time we will take one frame then process this frame
**cap.read():** return two results  ret: boolean True or False if read was done successfully (video source or camera is connected or not, video are end or no), and return the frame it self
**condition:** if video end or camera disconnect we exit from the loop

```python
 results = model.predict(
        source=frame,
        conf=config.conf_threshold,
        verbose=False
    )

```
### send frame to model by using predict() function

```python

    detected = False
    for result in results:
        if result.boxes is None:
            continue
```
### first we create a boolean start with false when the target class appear change it to True to make the action

**results:** from predict function return useful value such conf, xyxy: the object axis[] in frame
**result.boxes:** is most important part in predict function this part have the xyxy axis and all object info and more 
### Read more about [predict function](../../reference/yolo-results.md)
**condition :** if boxes is None, in other word **no object detect**, skip this iteration by **continue** key word while break will exit from the loop 

```python

  for class_id in result.boxes.cls.tolist():
      class_name = model.names[int(class_id)]
```
### This is second nested loop
**result.boxes.cls:** This is Tensor matrix include all id for each object, because maybe frame include more than one object, an example return [15,15], this number is id for the object name and 15 is cat in the model 
**tolist():** we use tolist() function to convert from <type> in this case is Tensor to normal list
**model.names[]:** from the dictionary you get value form key, (key:value), in YOLO the object save from ID -> Name, names{0:"person", 1: "bicycle", 2:"car"} and other id with names 

**.names[class_id]:** will return class name, an example if id is "15.0" we will get cat the **class name**, and we use int() to ensue number are int not a string  

```python
if class_name == config.target_class:
    detected = True
```
### if class name equal to target class which we was select first in Config class, make detected = True

```python
  if detected:
    # here add your action

```
### if detected is True this mean target class are appear, so we can make the action in this block    

```python
 if config.show_window:
    cv2.imshow("YOLO Camera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
```
**cv2.imshow(<Window name>, <video frame>):** display current video frame in a window, and the name of this window is selected by Window name **first parameter**

**cv2.waitKey(<read time>):** cv waits up to <read time>, an example if number is 1, this mean cv will read keyboard input every 1ms
**0xFF:** filter to ensue correct read key in all OS
**ord(<key>):** convert key into ASCll 


```python
cap.release()
cv2.destroyAllWindows()
```
**cap.release():** stop using camera **close the camera**
**cv2.destroyAllWindows():** close all open window