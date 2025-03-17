from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")


# Khởi tạo client Groq với API key
GROQ_CLIENT = Groq(api_key=api_key)  # Thay API key của bạn


def get_groq_client():
    """Trả về Groq Client đã được tạo"""
    return GROQ_CLIENT

def extract_invoice_details(extracted_text: str):
    # Prompt để yêu cầu Groq phân tích văn bản hóa đơn
    prompt = f"""
    Bạn là một trợ lý AI chuyên trích xuất thông tin từ hóa đơn. Dựa trên văn bản sau, \
        hãy trích xuất các thông tin chính như \
            Thông tin nhà cung cấp \
            Thông tin khách hàng \
            Thông tin hóa đơn \
            Chi tiết hóa đơn \
            Tổng cộng \
        các thông tin biểu diễn bằng tiếng Việt Nam \
        của hoá đơn sau:
 
    Văn bản hóa đơn:
    {extracted_text}
    """

    # Gửi yêu cầu tới Groq API
    client = get_groq_client()

    response = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
        ],
        model="llama-3.3-70b-versatile"        
    )

    # Lấy nội dung phản hồi từ Groq
    extracted_details = response.choices[0].message.content
    extracted_details = extracted_details.split("\n")

    return extracted_details