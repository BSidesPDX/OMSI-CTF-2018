TARGET=bfbo

CC=gcc
CFLAGS=-fno-stack-protector -zexecstack -m32

all: $(TARGET)
	strip bfbo

clean:
	@rm $(TARGET)
