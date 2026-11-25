FROM python@sha256:1e1f6334529d1fb26a2ef619d7cffb30a7c7d7cc1cc7338ebee283a58d1aeaca AS builder
# 3.13-slim
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM python@sha256:1e1f6334529d1fb26a2ef619d7cffb30a7c7d7cc1cc7338ebee283a58d1aeaca AS runner
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN adduser -S -u 10001 -h /app appuser
RUN mkdir /data && touch /data/visits.txt && chown appuser:nogroup /data/visits.txt
USER appuser
COPY --chown=appuser:nogroup app.py ./
EXPOSE 8080
CMD ["python", "app.py"]
