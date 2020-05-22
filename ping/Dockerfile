FROM python:3.7
WORKDIR /tmp/ping
COPY . .
RUN chmod -R 777 .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["/tmp/ping/app.py"]
