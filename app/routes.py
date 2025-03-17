from fastapi import APIRouter, UploadFile, File, Query
from app.services.ocr import extract_text_ocr
from app.services.groq import extract_invoice_details

from app.models.invoice import InvoiceResponse, ExtractedInvoice

router = APIRouter()

@router.post("/extract-invoice", response_model=ExtractedInvoice)
async def extract_invoice(file: UploadFile = File(...), use_google_vision: bool = Query(False)):
    file_bytes = await file.read()

    extracted_text = extract_text_ocr(file_bytes, file.filename)
    
    # Gọi DeepSeek để phân tích thông tin chính
    extracted_details = extract_invoice_details("\n".join(extracted_text))

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "invoice_details": extracted_details
    }
    
# Router xử lý yêu cầu POST và gọi hàm extract_invoice_details
@router.post("/invoice_details/")
async def extract_invoice(extracted_text: str):
    extracted_details = extract_invoice_details(extracted_text)
    return extracted_details
