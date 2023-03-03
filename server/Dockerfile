FROM python:3.7
COPY ./* ./app/
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "server.py"]
