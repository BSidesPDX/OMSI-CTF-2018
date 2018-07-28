FROM ubuntu:bionic

# Depens
run apt-get update
run apt-get install xinetd build-essential gcc-multilib -y
run apt-get clean

# Add files to container
WORKDIR /opt/
ADD flag /
ADD bfpl /opt/bfpl
ADD bfpl.service /etc/xinetd.d/bfpl

EXPOSE 10002

CMD ["xinetd", "-dontfork"]
