#!/usr/bin/env/python
from __future__ import print_function
import re
import time
import sys
import os
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
def main():
    print('\n1. Extracting emails from document')
    print('2. Exit')
    while True:
        try:
            choice = int(input('Enter choice: '))
            if choice == 1:
                extractor()
                break
            elif choice == 2:
                break
            else:
                print("Invalid choice. Enter 1 or 2")
                main()
        except ValueError:
            print("Invalid choice. Enter 1 or 2")
    exit()


def extractor():
    # regular expression to define the mail search pattern
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    user_input = input(">>>Enter the path to your file: ")

    # user screen starts with a slow printing output of 8 seconds
    def slowprint(drake):
        for n in drake + '\n':
            sys.stdout.write(n)
            sys.stdout.flush()
            time.sleep(8. / 100)

    slowprint("Starting email extraction... ")
    time.sleep(5)

    # raising user error message if path not valid
    assert os.path.exists(user_input), "No file to extract emails was found at, " + str(user_input)
    f = open(user_input, 'r')
    print("\n", r.choice(list(open('leaflets/spas.txt'))), "\n")

    match = re.findall(pattern, f.read())

    for elem in match:
        # Outputs identified emails(results) in the same program folder with a name match.txt
        sys.stdout = open("match.txt", "w")
        # sorting the output in a formatted list
        if match:
            print(*match, sep='\n')
            print("\n", "\n", "Emails successfully extracted. Goodbye!", "\n")
        else:
            print("\n", "No extractable emails found in the document", "\n")
 
        sys.stdout.close()


if __name__ == '__main__':
    main()
