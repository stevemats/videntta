#!/usr/bin/env/python
from __future__ import print_function
import re
import time
import sys
import os
import random as r

from assets.harvest_url import harvest_url as url_emails

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


# conditions are to prevent non-context keywordsbeig executed
def main():
    print('\n1. Extract emails from your txt document')
    print('2. Extract emails from a URL(Beta Version)')
    print('3. Exit')
    while True:
        try:
            choice = int(input('Enter choice: '))
            if choice == 1:
                extractor()
                break
            elif choice == 2:
                url_emails()
                break
            elif choice == 3:
                break
            else:
                print("Invalid choice. Enter a choice in menu. 1, 2 or 3")
                main()
        except ValueError:
            print("Invalid choice. Enter 1, 2 or 3")
    exit()


def extractor():
    # regular expression to define the mail search pattern
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    user_input = input(">>>Enter the path to your file: ")

    def email_list_to_text(emails):
        text = ''
        for email in emails:
            text += '{}\n'.format(email)
        return text

    # slow printing output in seconds
    slow_speed = 8. / 100

    def slowprint(drake):
        for n in drake + '\n':
            sys.stdout.write(n)
            sys.stdout.flush()
            time.sleep(slow_speed)

    slowprint("Starting email extraction... ")
    time.sleep(5)

    # raising user error message if path not valid
    assert os.path.exists(user_input), "No file to extract emails was found at, " + str(user_input)
    f = open(user_input, 'r')
    print("\n", r.choice(list(open('leaflets/spas.txt'))), "\n")

    match = re.findall(pattern, f.read())

    output = email_list_to_text(match)

    # added feature to sort out the email in list
    # Outputs identified emails(results) in the same program folder with a name match.txt
    extensionTime = time.strftime("%m_%d_%Y")
    myFile = "emailDump_"+extensionTime+".txt"
    
    with open(myFile, 'w') as match_file:
        match_file.write(output)

    if match:
        print("{} emails successfully extracted:\n\n{} ".format(len(match), output))
    else:
        print("\n", "No extractable emails found in the document", "\n")

def exit():
    print('\n','Program closed. GoodBye!')


if __name__ == '__main__':
    main()
