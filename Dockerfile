FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3.8 python3-pip -y

ADD ./api/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

RUN mkdir opt/api
ARG project_dir=/opt/api
ADD ./api $project_dir

WORKDIR $project_dir

# run flask app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
