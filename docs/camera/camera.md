# Camera

[← Back to Home](../../README.md)


###
```python
model.predict(
    source=0,
    show=True,
    conf=0.5
)
```

**model = YOLO(model_path):** I explain this before we invoke the model to use it now
**model.predict():** is a function take a lot of parameters but for now its take only 3 parameter
- **source:** is the input source, we can add a photo path, or video, but here we use camera so the index is 0, if you have multiple camera maybe you need to change index in this range {0,1,2,...,n}
- **show:** take a boolean for open a window to show video with the boxes and class name
- **conf:** or Confidence Threshold, is the percentage of trust this object is Confident from it more than 50%, when we use small conf every object well appear even if model not sure what is this 


