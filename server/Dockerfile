FROM python:3.7
COPY ./* ./app/
COPY ./PyChatGPT/* ./app/PyChatGPT/
COPY ./PyChatGPT/Classes/* ./app/PyChatGPT/Classes/
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["waitress-serve"]
CMD ["--port=8080", "--call", "server:application"]