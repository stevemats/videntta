
import re

pattern = r'[\w\.-]+@[\w\.-]+'
str = '''Tom and jerry logged in as john@gmail.com at the site which they used to meet bout nuclear energy
        collect all the emails and present them before 2300 military hrs. Send the results to energy@mail.com'''

match = re.findall(pattern, str)
#use findall where there's need to extract more than one email
if match:
    print(match)

print ("Emails successfully extracted. Goodbye!")

