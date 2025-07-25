
FROM python:3.10-slim


RUN apt-get update && apt-get install -y \
    poppler-utils \
 && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src/ ./src/
COPY models/ ./models/
COPY input_docs/ ./input_docs/


CMD ["python", "src/main.py"]
