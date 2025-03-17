import requests
import json
#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
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

client = Groq(
    api_key=api_key
)

text = """CÔNG TY CỔ PHẦN THẾ GIỚI DI ĐỘNG
 128 Trần Quang Khải, Phường Tân Định, Quận 1, Thành phố Hồ Chí Minh, Việt Nam
 Mã số thuế: 0303217354
 Điện thoại: 1800 1061(Bán hàng) - 1800 1063(Khiếu nại) - 1800 1065(Bảo hành)
 Tài khoản số: 044.100.061.5156  Ngân hàng: VCB_CN Tân Bình, HCM
 HÓA ĐƠN
 6893076 GIÁ TRỊ GIA TĂNG Số: 
Mẫu số: 01GTKT0/007
 Ký hiệu: AB/20E
 Ngày: 14/10/2021 (HÓA ĐƠN CHUYỂN ĐỔI TỪ HÓA ĐƠN ĐIỆN TỬ)
 Tên hàng hoá, dịch vụ Đơn vị tính Thuế suất 
(%)
 Số lượng Đơn giá
 Hình thức thanh toán:  CK / TM / Cấn trừ công nợ
 STT Thành tiền
 Địa chỉ: 47-49-51 Đường Phùng Khắc Khoan, Phường Đa Kao, Quận 1, Thành phố Hồ Chí 
Minh  Read more: 
https://masocongty.vn/company/2652157/cong-ty-tnhh-viet-nam-crane-service.html#ixzz79G
 Mã số thuế: 0315569167
 Họ tên người mua hàng: 
Tên đơn vị : CÔNG TY TNHH VIỆT NAM CRANE SERVICE
 3 4 5 6 7=5 x 6 1 2
 Tên CN: CHI NHÁNH CÔNG TY CỔ PHẦN THẾ GIỚI DI ĐỘNG - 
CỬA HÀNG ĐIỆN MÁY XANH 137 QUỐC LỘ 13
 Địa chỉ CN: 137 Quốc Lộ 13, Phường Hiệp Bình Chánh, Thành 
phố Thủ Đức, Thành phố Hồ Chí Minh, Việt Nam
 Mã số thuế: 0303217354 ĐT: 0909929003
 Office Home and Student 2021 All Lng APAC EM PK Lic 
Online DwnLd NR (79G-05337) - Mới
 Cái 10% 1 1.990.909 1 1.990.909
 Tiền hàng hoá, dịch vụ
 Tiền thuế
 Tiền thanh toán
 Thuế suất 0% Thuế suất 5% Thuế suất 10% Tổng cộng
 0 0 1.990.909 1.990.909
 199.091
 2.190.000
 0 199.091
 0 2.190.000
 Bên mua
 (Ký, ghi rõ họ tên)
 Mã CTCĐ: Người chuyển đổi: 145915 - Nguyễn Thị Thúy Thương Ngày chuyển đổi: 14/10/
 (Cần kiểm tra đối chiếu khi lập, giao, nhận hóa đơn)
 Số tiền bằng chữ:
 0
 0
 Không chịu thuế
 0
 0
 x
 Bên bán
 ü Ký điện tử bởi: CÔNG TY CỔ PHẦN THẾ GIỚI DI 
ĐỘNG
 Khách hàng vào web https://hddt.thegioididong.com để tải về hóa đơn điện tử
 Hai triệu một trăm chín mươi nghìn đồng chẵn
 Serial number: 54010108694C2E0B1B347E4553C4655C
 Ký ngày: 14/10/2021, Hãy trích xuất các thông tin quan trọng của hoá đơn trên"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": text,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)