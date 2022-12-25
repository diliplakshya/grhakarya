FROM python:3.8.16-slim-buster
WORKDIR /app
EXPOSE 5000
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
