#!/usr/bin/python3

'''
Make the flag for sgnirts
'''

import sys
import string
import random

def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

counter = 0
iterator = 5

flagFile = open("flag", "r").readline().rstrip('\n')
challenge = open("sgnirts.c", "w+")

challenge.write("#include <stdio.h>\n");

while counter < 1000:
    if not counter%100:
        iterator += 1
    flagVal = id_generator(iterator,  string.ascii_uppercase + string.digits + string.ascii_lowercase)
    if counter == 514:
        flagVal = flagFile
    starter = "char *a" + str(counter) + "= \"BSidesPDX{" + flagVal
    challenge.write(starter + "}\";\n")
    counter += 1

challenge.write("void main() { printf(\"you can do it\\n\"); } \n");
