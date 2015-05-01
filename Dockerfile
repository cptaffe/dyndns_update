
FROM debian

# install appropriate packages
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip

# install requirements
RUN pip3 install requests

CMD ./dyndns_update.py
