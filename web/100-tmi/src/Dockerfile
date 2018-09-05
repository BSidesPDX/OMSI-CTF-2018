FROM ubuntu:bionic

# Depens
run apt-get update
run apt-get install -y python-pip
run apt-get clean
run pip install flask

# Add files to container
WORKDIR /opt/
ADD flag /opt/flag
ADD password /opt/password
ADD index.html /opt/index.html
ADD tmi.py /opt/tmi.py

EXPOSE 5000

CMD ["python", "-m", "tmi"]
