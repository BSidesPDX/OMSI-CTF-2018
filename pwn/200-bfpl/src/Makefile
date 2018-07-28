TARGET=bfpl

CC=gcc
CFLAGS=-fno-stack-protector -zexecstack -m32

all: $(TARGET)
	strip $(TARGET)

clean:
	@rm $(TARGET)
