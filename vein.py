#!/usr/bin/env/python
import re
import sys

pattern = r'[\w\.-]+@[\w\.-]+'
f = open('data/info.txt', 'r')

match = re.findall(pattern, f.read())

if match:
    print(match)

print("\n")    
print ("Emails successfully extracted. Goodbye!")

