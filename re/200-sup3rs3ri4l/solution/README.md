# RE 200 Solution

There are several ways to solve this binary. One is to look at the control flow and do an xrefs on the 3 string variables used to make the serial. Others are to just just strings and see all the instances of 4 characters to make up the serial.

```
strings serial
1337
dead
beef
Please enter serial
Serial is correct
Incorrect serial
The serial must be in the format of BSidesPDX{XXXX_XXXX_XXXX}

./serial
Please enter serial
BSidesPDX{1337_dead_beef}
Serial is correct
```
