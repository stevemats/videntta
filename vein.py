#!/usr/bin/env/python
import re
import sys, os
import random as r

print('''


                                            __
      o                 /' ) 
                      /'   (                          ,
                  __/'     )                        .' `;
   o      _.-~~~~'          ``---..__             .'   ;
     _.--'  b)                       ``--...____.'   .'
    (     _.      )).      `-._                     <  free nation!!
     `\|\|\|\|)-.....___.-     `-.         __...--'-.'.
 stv   `---......____...---`.___.'----... .'         `.;
                                        `-`           `  
''')


# pattern to use to find valid emails and path to user data
# introduced and defined as user input

pattern = r'[\w\.-]+@[\w\.-]+'
user_input = input("Enter the path to your file: ");

'''
exception when the input path is invalid defining the file to read 
from the user input and a print success containing a list to print
on a random upon a successful extraction of emails
'''
assert os.path.exists(user_input), "No file to extract emails was found at, "+str(user_input)
f = open(user_input, 'r')
print("\n", r.choice(list(open('leaflets/spas.txt'))),"\n")

match = re.findall(pattern, f.read())

'''
printing out the extracted emails to our desired destination document
and introducing clauses for our successful/unseccessful extractions
'''
sys.stdout=open("match.txt","w")
if match:
    print(match, "\n","\n","Emails successfully extracted. Goodbye!", "\n")
else:
    print("\n", "No extractable emails found in the document", "\n")
    
sys.stdout.close()    
