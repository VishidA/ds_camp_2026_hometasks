from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn
import requests
import numpy as np
import cv2
from PIL import Image
import io
import gradio as gr
from model import MyModel

API_URL = "http://127.0.0.1:8000/api/detect"
app = FastAPI(title="YOLOv8 Detection API")
model = MyModel()


@app.post("/api/detect")
def detect(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File should be an image")

    try:
        image_bytes = file.file.read()
        detections = model.predict(image_bytes)
        return {
            "filename": file.filename,
            "objects_found": len(detections),
            "detections": detections
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def predict_via_api(image: np.ndarray):
    if image is None:
        return None

    pil_img = Image.fromarray(image)
    buf = io.BytesIO()
    pil_img.save(buf, format="JPEG")
    buf.seek(0)

    response = requests.post(
        API_URL,
        files={"file": ("image.jpg", buf, "image/jpeg")}
    )
    response.raise_for_status()
    detections = response.json()["detections"]

    result_img = image.copy()
    for det in detections:
        x1, y1, x2, y2 = map(int, det["bbox"])
        cv2.rectangle(result_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        label = f'{det["class"]} {det["confidence"]}'
        cv2.putText(result_img, label, (x1, max(y1 - 5, 0)),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    return result_img


demo = gr.Interface(
    fn=predict_via_api,
    inputs=gr.Image(type="numpy", label="Upload image"),
    outputs=gr.Image(type="numpy", label="Result"),
    title="Image classification",
)

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)