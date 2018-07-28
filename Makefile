target: pwn

pwn:
	make -C ./pwn/100-bfbo/src
	make -C ./pwn/200-bfpl/src

clean:
	make -C ./pwn/100-bfbo/src clean
	make -C ./pwn/200-bfpl/src clean
