import re
from requests_html import HTMLSession


def harvest_url():
    url = input(">>>Enter URL to extract emails: ")
    REGEX_PATTERN = r'[\w\.-]+@[\w\.-]+\.\w+'

    # initiate an HTTP session
    session = HTMLSession()
    # get the HTTP Response
    r = session.get(url)
    # for JAVA-Script driven websites
    r.html.render()

    for re_match in re.finditer(REGEX_PATTERN, r.html.raw_html.decode()):
        print(re_match.group())

if __name__ == '__main__':
    harvest_url()