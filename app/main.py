from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI(title="Invoice Extraction API")

# Cấu hình CORS để cho phép frontend truy cập API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hoặc ["http://127.0.0.1:8000"] nếu muốn giới hạn
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả phương thức (GET, POST, ...)
    allow_headers=["*"],  # Cho phép tất cả headers
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def home():
    return RedirectResponse(url="/static/index.html")

# Định nghĩa các route
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
