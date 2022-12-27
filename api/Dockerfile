FROM python:3.11.1-slim-buster
WORKDIR /app
EXPOSE 5000
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# ARG DB_URL=${DB_URL}
# ENV DB_URL=${DB_URL}
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
