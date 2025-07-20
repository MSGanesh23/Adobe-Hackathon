
FROM --platform=linux/amd64 python:3.10-slim


WORKDIR /app


COPY . .


RUN apt-get update && \
    apt-get install -y libglib2.0-0 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt


ENV PYTHONDONTWRITEBYTECODE=1


CMD ["python", "cli.py"]
