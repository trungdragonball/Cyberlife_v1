import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

app = FastAPI()

# Cấu hình CORS để cho phép Frontend gửi truy vấn
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    owner_id: Optional[str] = "default_user"

@app.post("/api/v1/chat")
async function chat_endpoint(req: ChatRequest):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"response": "Lỗi: Chưa cấu hình GEMINI_API_KEY trong file .env"}

    try:
        # Khởi tạo client kết nối tới Gemini API
        client = genai.Client(api_key=api_key)
        
        # Gọi mô hình Gemini 2.5 Flash
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=req.message,
        )
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Lỗi xử lý API: {str(e)}"}
