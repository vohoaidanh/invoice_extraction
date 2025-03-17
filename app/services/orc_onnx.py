import cv2
import numpy as np
import onnxruntime as ort
from pdf2image import convert_from_bytes

from app.nets import nn
from app.utils import util

detection = nn.Detection('app/models/onnx/detection.onnx')
#recognition = nn.Recognition('app/models/onnx/recognition.onnx')
classification = nn.Classification('app/models/onnx/classification.onnx')

recognition = nn.Recognition('app/models/onnx/en_PP-OCRv3_rec_infer.onnx')

def resize_with_aspect_ratio(img, target_height=32):
    """Resize ảnh sao cho chiều cao = target_height nhưng giữ nguyên tỷ lệ"""
    h, w = img.shape[:2]
    scale = target_height / h  # Tính tỷ lệ resize
    new_w = int(w * scale)  # Tính chiều rộng mới theo tỷ lệ
    resized_img = cv2.resize(img, (new_w, target_height), interpolation=cv2.INTER_AREA)
    return resized_img


def extract_text_ocr(file_bytes: bytes, filename: str):
    file_extension = filename.split(".")[-1].lower()
    
    if file_extension == "pdf":
        images = convert_from_bytes(file_bytes)
        img = np.array(images[0])  # Lấy trang đầu tiên của PDF
    else:
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    if img.shape[0] > 1200:  # Kiểm tra height
        img = resize_with_aspect_ratio(img, target_height=1200)

    points = detection(img)
    points = util.sort_polygon(list(points))


    cropped_images = [util.crop_image(img, x) for x in points]
    cropped_images, angles = classification(cropped_images)
    results, confidences = recognition(cropped_images)

    extracted_text = results
    print(extracted_text)
    return extracted_text
