// PWN-200-BFPL BSidesPDX OMSI CTF

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

#define disable_buffering(_fd) setvbuf(_fd, NULL, _IONBF, 0)
#define LEN 256

void disable_buf()
{
	disable_buffering(stdout);
	disable_buffering(stderr);
}

void main()
{
	int len;
    void (*shellcode)(void);
    
    disable_buf();

    shellcode = mmap(NULL, LEN, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, 0, 0);
    
    memset(shellcode, 0xCC, LEN); //memset shellcode with NOPS

	printf("Enter a string: \n");
    
    len = read(0, shellcode, LEN+1);
    if(len < 0) 
    {
        printf("I didn't get your string!\n");
        exit(1);
    }

    printf("I will run for you %s\n", shellcode);

    __asm__ ("call *%0\n" 
    : 
    :"r"(shellcode)); //input);
}
