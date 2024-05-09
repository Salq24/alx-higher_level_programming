#!/bin/bash
#takes in a url, sends a request to the url, displays the body size
curl -s "$1" | wc -c
