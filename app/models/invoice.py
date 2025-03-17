from pydantic import BaseModel
from typing import List, Dict

class InvoiceResponse(BaseModel):
    filename: str
    extracted_text: List[str]

class ExtractedInvoice(BaseModel):
    filename: str
    extracted_text: List[str]
    invoice_details: List[str]  # Kết quả từ DeepSeek API