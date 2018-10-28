#!/usr/bin/env/python
import re
import sys

print('''


                                            __
      o                 /' ) 
                      /'   (                          ,
                  __/'     )                        .' `;
   o      _.-~~~~'          ``---..__             .'   ;
     _.--'  b)                       ``--...____.'   .'
    (     _.      )).      `-._                     <
     `\|\|\|\|)-.....___.-     `-.         __...--'-.'.
 jgs   `---......____...---`.___.'----... .'         `.;
                                        `-`           `  
''')

pattern = r'[\w\.-]+@[\w\.-]+'
f = open('data/info.txt', 'r')

match = re.findall(pattern, f.read())

if match:
    print(match)

print("\n")    
print ("Emails successfully extracted. Goodbye!", "\n")
else:
    print("\n", "No extractable emails found in the document", "\n")

