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
print("\n",  "Emails have been successful extracted, checkout the output in the program folder", "\n")

pattern = r'[\w\.-]+@[\w\.-]+'
f = open('data/info.txt', 'r')

match = re.findall(pattern, f.read())

sys.stdout=open("match.txt","w")
if match:
    print(match, "\n","\n","Emails successfully extracted. Goodbye!", "\n")
else:
    print("\n", "No extractable emails found in the document", "\n")
    
sys.stdout.close()    
