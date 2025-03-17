import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_bytes
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")  # Hỗ trợ tiếng Anh, có thể đổi sang 'vi'

def extract_text_ocr(file_bytes: bytes, filename: str):
    file_extension = filename.split(".")[-1].lower()

    if file_extension == "pdf":
        images = convert_from_bytes(file_bytes)
        img = np.array(images[0])  # Lấy trang đầu tiên
    else:
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Sử dụng PaddleOCR để nhận diện văn bản
    results = ocr.ocr(img, cls=True)
    extracted_text = [word[1][0] for line in results for word in line]

    return extracted_text
