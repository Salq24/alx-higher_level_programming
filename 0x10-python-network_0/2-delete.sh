#!/bin/bash
#sends a DELETE request to the URL passed as the first argument,displays response body
curl -sX DELETE "$1"
