FROM python@sha256:1e1f6334529d1fb26a2ef619d7cffb30a7c7d7cc1cc7338ebee283a58d1aeaca 
# 3.13-slim
WORKDIR /app
RUN adduser -S -u 10001 appuser
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser app.py ./
USER appuser
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]
