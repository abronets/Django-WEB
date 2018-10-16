FROM mediasapiens/python3

WORKDIR /web
COPY requirements.txt /requirements.txt

RUN pip install -U pip
RUN pip install -r /requirements.txt --ignore-installed
