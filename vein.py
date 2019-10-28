#!/usr/bin/env/python
from __future__ import print_function
import re
import time
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

# regular expression to define the search pattern
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
user_input = input(">>>Enter the path to your file: ");

def email_list_to_text(emails):
    text = ''
    for email in emails:
        text += '{}\n'.format(email)
    return text

# user screen starts with a slow printing output of 8 seconds
def slowprint(videntta):
    for n in videntta + '\n' :
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(8. / 100)
slowprint("Starting email extraction... ")
time.sleep(5)

# raising user error message if path not valid
assert os.path.exists(user_input), "No file to extract emails was found at, "+str(user_input)
f = open(user_input, 'r')
print("\n", r.choice(list(open('leaflets/spas.txt'))),"\n")

match = re.findall(pattern, f.read())

output = email_list_to_text(match)

# Outputs identified emails(results) in the same program folder with a name match.txt
with open('match.txt','w') as match_file:
    match_file.write(output)

if match:
    print("{} emails successfully extracted:\n\n{} ".format(len(match), output))
else:
    print("\n", "No extractable emails found in the document", "\n")
