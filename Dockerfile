
FROM debian

# install appropriate packages
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip

# install requirements
COPY requirements.txt /tmp/
RUN pip3 install /tmp/requirements.txt
COPY . /tmp/

CMD ./dyndns_update.py
