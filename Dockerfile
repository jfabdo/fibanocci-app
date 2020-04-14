FROM python:alpine3.7

COPY requirements.txt /
RUN pip3 install -r requirements.txt

ADD src /src
WORKDIR /src
RUN chmod +x /src/entrypoint.sh

ENV ALLOWED_ORIGINS '["*"]'
ENV LOG_LEVEL INFO
ENV FLASK_HOST localhost
ENV FLASK_PORT 8080

CMD ["/src/entrypoint.sh"]
