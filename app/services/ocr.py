import cv2
import numpy as np
from pdf2image import convert_from_bytes
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, 
                rec_algorithm='CRNN', 
                det_db_box_thresh=0.5, 
                lang="en",
                rec_model_dir="app/models/en_PP-OCRv3_rec_slim_infer")  # Hỗ trợ tiếng Anh, có thể đổi sang 'vi'

def resize_with_aspect_ratio(img, target_height=512):
    """ Resize ảnh sao cho chiều cao = target_height nhưng giữ nguyên tỷ lệ """
    h, w = img.shape[:2]
    scale = target_height / h  # Tính tỷ lệ resize
    new_w = int(w * scale)  # Tính chiều rộng mới theo tỷ lệ
    resized_img = cv2.resize(img, (new_w, target_height), interpolation=cv2.INTER_AREA)
    return resized_img

def extract_text_ocr(file_bytes: bytes, filename: str):
    file_extension = filename.split(".")[-1].lower()

    if file_extension == "pdf":
        images = convert_from_bytes(file_bytes)
        img = np.array(images[0])  # Lấy trang đầu tiên
    else:
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        #img = resize_with_aspect_ratio(img, target_height=800)

    # Sử dụng PaddleOCR để nhận diện văn bản
    

    results = ocr.ocr(img, cls=True)
    extracted_text = [word[1][0] for line in results for word in line]

    return extracted_text
