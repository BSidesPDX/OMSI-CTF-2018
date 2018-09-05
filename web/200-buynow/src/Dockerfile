FROM ubuntu:bionic

# Depens
run apt-get update
run apt-get install -y python-pip
run apt-get clean
run pip install flask

# Add files to container
WORKDIR /opt/
ADD flag /opt/flag
ADD buynow.py /opt/buynow.py

EXPOSE 5000

CMD ["python", "-m", "buynow"]
