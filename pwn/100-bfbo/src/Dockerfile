FROM ubuntu:bionic

# Depens
run apt-get update
run apt-get install xinetd build-essential gcc-multilib -y
run apt-get clean

# Add files to container
WORKDIR /opt/
ADD flag /
ADD bfbo /opt/bfbo
ADD bfbo.service /etc/xinetd.d/bfbo

EXPOSE 10001

CMD ["xinetd", "-dontfork"]
