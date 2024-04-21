FROM alpine:3.19

RUN apk add --no-cache python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt --break-system-packages

CMD ["python3", "src/main.py"]
