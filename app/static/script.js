function uploadFile() {
    let fileInput = document.getElementById("fileInput").files[0];
    let uploadButton = document.getElementById("uploadButton");

    if (!fileInput) {
        alert("Vui lòng chọn một file hóa đơn!");
        return;
    }
    uploadButton.disabled = true;
    let formData = new FormData();
    formData.append("file", fileInput);

    // Hiển thị spinner loading khi đang xử lý
    const loadingElement = document.getElementById('loading');
    loadingElement.classList.remove('d-none');  // Hiển thị spinner

    document.getElementById("resultText").value = "";

    fetch("/extract-invoice", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Ẩn spinner khi quá trình hoàn tất
        loadingElement.classList.add('d-none');
        
        // Kiểm tra nếu response trả về có dữ liệu hóa đơn
        if (data && data.invoice_details) {
            document.getElementById("resultText").value = data.invoice_details.join("\n");
        } else {
            alert("Không tìm thấy dữ liệu hóa đơn trong file!");
        }
    })
    .catch(error => {
        console.error("Lỗi:", error);
        loadingElement.classList.add('d-none'); // Ẩn spinner khi có lỗi
        alert("Có lỗi xảy ra! Vui lòng thử lại.");
    })
    .finally(() => {
        // Kích hoạt lại nút khi quá trình hoàn tất
        uploadButton.disabled = false;  // Enable lại nút
        document.getElementById("loading").classList.add("d-none");  // Ẩn biểu tượng loading
    });
    
}
