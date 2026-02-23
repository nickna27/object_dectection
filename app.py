import streamlit as st
import cv2
from ultralytics import YOLO

st.set_page_config(layout="wide")
st.title("Face Mask Detection - YOLOv8 Realtime")

model_link = "YOUR_MODEL_LINK"

model = YOLO(model_link)   
model.to("cpu")           
run = st.button("Turn on the Camera")
FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Cannot access the camera")
        break


    frame = cv2.resize(frame, (640, 480))

 
    results = model.predict(
        source=frame,
        imgsz=416,      
        conf=0.4,
        device="cpu",
        verbose=False
    )

    annotated_frame = results[0].plot()


    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    FRAME_WINDOW.image(annotated_frame)

cap.release()
