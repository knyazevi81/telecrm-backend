FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

COPY . /app

COPY entrypoin.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# run the script via the shell to avoid exec-format/shebang quirks
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
