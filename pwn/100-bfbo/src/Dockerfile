FROM ubuntu:xenial

# Depens
run apt-get update
run apt-get install xinetd build-essential gcc-multilib -y
run apt-get clean

# Add files to container
WORKDIR /opt/
ADD flag /
ADD bfbo /opt/bfbo
ADD bfbo.service /etc/xinetd.d/bfbo

# Make and Run
run echo "bfbo 1001/tcp" >> /etc/services
EXPOSE 1001

CMD ["xinetd", "-dontfork"]
