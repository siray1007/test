FROM    python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY . .
CMD ["python", "app.py"]
EXPOSE 5000
