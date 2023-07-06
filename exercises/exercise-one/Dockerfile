FROM alpine:3.18.2
LABEL maintainer="mrmonkey82@gmail.com"
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
COPY ./app /src
WORKDIR /src
RUN pip3 install -r requirements.txt
EXPOSE 8080
RUN python3 main.py