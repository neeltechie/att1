FROM python:3.7
WORKDIR /tmp/pong
COPY . .
RUN chmod -R 777 .
RUN pip install -r requirements.txt
EXPOSE 6000
CMD ["/tmp/pong/app.py"]
