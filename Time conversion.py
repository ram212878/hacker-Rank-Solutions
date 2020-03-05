#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    string=""
    if "AM" in s:
        if s[:2]=="12":
            return "00"+s[2:-2]
        else:
            return s[0:-2]      
    elif s[0:2]!="12":
        return str(int(s[:2])+12)+s[2:-2]
    else:
        return s[0:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result+'\n')

    f.close()
