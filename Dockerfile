FROM python:3.10-slim

WORKDIR /app

# Cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# Mở cổng 8080 cho Render
EXPOSE 8080

# Chạy Gradio
CMD ["python", "app.py"]
