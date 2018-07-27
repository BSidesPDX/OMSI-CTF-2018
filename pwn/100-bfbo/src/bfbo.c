// PE-100-BFBO BSidesPDX OMSI CTF
// gcc bfbo.c -o bfbo -fno-stack-protector -z execstack -m32

#include <stdio.h>
#include <stdlib.h>

int main()
{
  char buf[20];
  long val=0x41414141;
  FILE *flag;
  char ch;

  printf("Do you folks like 0xc0ff33?");
  scanf("%24s",&buf);

  printf("buf: %s\n",buf);
  printf("val: 0x%08x\n",val);

  if(val==0xc0ff33)
  {
    flag = fopen("/flag", "r");
    if (flag == NULL)
    {
      printf("Cannot open file\n");
      exit(0);
    }
    printf("Real 0xc0ff33, from the hills of\n");
    ch = fgetc(flag);
    while (ch != EOF)
    {
      printf("%c", ch);
      ch = fgetc(flag);
    }
  }
  else
  {
    printf("That is not how you drink 0xc0ff33\n");
    exit(1);
  }
  return 0;
}
