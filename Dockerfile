FROM python:3.10.1
ADD . /implementations
WORKDIR /
RUN python -m pip install -r requirements.txt
EXPOSE 57633