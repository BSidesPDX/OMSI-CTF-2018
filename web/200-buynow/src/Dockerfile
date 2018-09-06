FROM ubuntu:bionic

# Depens
run apt-get update
run apt-get install -y python-pip fonts-freefont-ttf fortune-mod
run apt-get clean
run pip install flask
run pip install sqlalchemy
run pip install flask-sqlalchemy
run pip install pillow
run mkdir /data

# Add files to container
WORKDIR /opt/
ADD index.html /opt/index.html
ADD hints /opt/hints
ADD flag /opt/flag
ADD buynow.py /opt/buynow.py

EXPOSE 5001

CMD ["python", "-m", "buynow"]
