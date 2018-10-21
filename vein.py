#!env/bin/python
import re
import sys

pattern = r'[\w\.-]+@[\w\.-]+'
f = open('secret/samp.txt', 'r')

match = re.findall(pattern, f.read())

if match:
    print(match)

print("\n")    
print ("Emails successfully extracted. Goodbye!")

