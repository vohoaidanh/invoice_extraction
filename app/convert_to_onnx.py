import os

# Thư mục chứa model PaddleOCR
MODEL_DIR = "app/models/en_PP-OCRv3_rec_infer"

# Thư mục lưu model ONNX
ONNX_DIR = "app/models/onnx"
os.makedirs(ONNX_DIR, exist_ok=True)

# Tên file PaddleOCR
MODEL_FILE = "inference.pdmodel"
PARAMS_FILE = "inference.pdiparams"

# Tên file đầu ra ONNX
ONNX_FILE = os.path.join(ONNX_DIR, "en_PP-OCRv3_rec_infer.onnx")

# Lệnh chuyển đổi PaddleOCR -> ONNX
command = f"""
paddle2onnx --model_dir {MODEL_DIR} \
--model_filename {MODEL_FILE} \
--params_filename {PARAMS_FILE} \
--save_file {ONNX_FILE} \
--opset_version 11 \
--enable_onnx_checker True
"""

# Chạy lệnh
os.system(command)

print(f"✅ Model đã được chuyển đổi thành công: {ONNX_FILE}")
