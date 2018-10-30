#!/usr/bin/env/python
import re
import sys
import random as r

print('''


                                            __
      o                 /' ) 
                      /'   (                          ,
                  __/'     )                        .' `;
   o      _.-~~~~'          ``---..__             .'   ;
     _.--'  b)                       ``--...____.'   .'
    (     _.      )).      `-._                     <
     `\|\|\|\|)-.....___.-     `-.         __...--'-.'.
 stv   `---......____...---`.___.'----... .'         `.;
                                        `-`           `  
''')
print("\n", r.choice(list(open('leaflets/spas.txt'))),"\n")

pattern = r'[\w\.-]+@[\w\.-]+'
f = open('data/info.txt', 'r')

match = re.findall(pattern, f.read())

sys.stdout=open("match.txt","w")
if match:
    print(match, "\n","\n","Emails successfully extracted. Goodbye!", "\n")
else:
    print("\n", "No extractable emails found in the document", "\n")
    
sys.stdout.close()    
