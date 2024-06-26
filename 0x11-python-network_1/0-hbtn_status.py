#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib"""


import urllib.request
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode("utf-8"))
