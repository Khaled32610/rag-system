# 1. تحديد بيئة التشغيل
FROM python:3.11-slim

WORKDIR /app

# 2. تحديث pip
RUN pip install --upgrade pip

# 3. استخدام ميزة الـ Cache Mount لحفظ الـ torch فور تحميله للأبد
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=1000 --retries 10 torch --index-url https://download.pytorch.org/whl/cpu

# 4. نسخ ملف المكتبات
COPY requirements.txt .

# 5. استخدام الـ Cache Mount لتثبيت باقي المكتبات وحفظ كاش لها
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=1000 --retries 10 -r requirements.txt

# 6. نسخ باقي ملفات المشروع
COPY . .

# 7. تشغيل السيرفر
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]