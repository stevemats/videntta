#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

try:
    from requests_html import HTMLSession
except ImportError:
    import os
    print ("requests_html isn\'t installed, installing now...")
    os.system('python -m pip install --user requests-html')
    print ('requests-html has been installed, restarting the program..')

def harvest_url():
    url = input(">>>Enter URL to extract emails: ")
    REGEX_PATTERN = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

    # initiate an HTTP session

    session = HTMLSession()

    # get the HTTP Response

    r = session.get(url)

    # for JS driven websites

    r.html.render()

    for re_match in re.finditer(REGEX_PATTERN, 
                                r.html.raw_html.decode()):
        print(re_match.group())

if __name__ == '__main__':
    harvest_url()
