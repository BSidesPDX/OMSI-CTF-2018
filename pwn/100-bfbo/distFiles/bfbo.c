// PE-100-BFBO BSidesPDX OMSI CTF

#include <stdio.h>
#include <stdlib.h>

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
