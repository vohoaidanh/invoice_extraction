#!/bin/bash
chmod +x main.py  # Cấp quyền chạy nếu cần
uvicorn app.main:app --host 0.0.0.0 --port $PORT
