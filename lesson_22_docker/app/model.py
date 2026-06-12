from ultralytics import YOLO
import io
from PIL import Image

class MyModel():

    def __init__(self, model_version: str = 'yolov8m.pt'):
        self.model = YOLO(model_version)

    def predict(self, image_bytes: bytes):
        
        if image_bytes is None:
            raise Exception("Image not found, try again")
        
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        results = self.model(image)

        detections = []
        
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                conf = box.conf[0].item()
                cls_id = int(box.cls[0].item())
                class_name = self.model.names[cls_id]

                detections.append({
                    "class": class_name,
                    "confidence": round(conf, 4),
                    "bbox": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)]
                })

        return detections        
    