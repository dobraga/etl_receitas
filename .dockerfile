FROM python:3
FROM selenium/standalone-chrome

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /app .

CMD ["python", "/app/scripts/malha.py"]