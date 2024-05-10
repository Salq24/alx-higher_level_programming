#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status using status"""
import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    bdy = response.text
    print("Body response:")
    print("\t- type:", type(bdy))
    print("\t- content:", bdy)
