#well well well another season new stuffs! |
#hollards delete! delete! slogan will be replaced today by:
#findall! extractall! findall! extractall!
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Tom and jerry logged in as john@gmail.com at the site which they used to meet bout nuclear energy "

match = re.search(pattern, str)
#use findall where there's need to extract more than one email
if match:
    print(match.group())
