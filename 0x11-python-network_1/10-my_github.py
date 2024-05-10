#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    usr_nm = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(usr_nm, passwd)

    res = requests.get(url, auth=auth)
    print(res.json().get('id'))
