// PE-100-BFBO BSidesPDX OMSI CTF
// gcc bfbo.c -o bfbo -fno-stack-protector -z execstack -m32

#include <stdio.h>
#include <stdlib.h>

#define disable_buffering(_fd) setvbuf(_fd, NULL, _IONBF, 0)

void disable_buf()
{
  disable_buffering(stdout);
  disable_buffering(stderr);
}

void printFlag()
{
  FILE *flag;
  char ch;

  flag = fopen("/flag", "r");
  if (flag == NULL)
  {
    printf("Cannot open file\n");
    exit(0);
  }
  ch = fgetc(flag);
  while (ch != EOF)
  {
    printf("%c", ch);
    ch = fgetc(flag);
  }
}

int main()
{
  char buf[20];
  long val=0x41414141;

  disable_buf();

  printf("Do you folks like 0xc0ff33?");
  scanf("%24s",&buf);

  printf("buf: %s\n",buf);
  printf("val: 0x%08x\n",val);

  if(val==0xc0ff33)
  {
    printFlag();
  }
  else
  {
    printf("That is not how you drink 0xc0ff33\n");
    exit(1);
  }
  return 0;
}
