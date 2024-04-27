#!/usr/bin/python3

"""
This takes in an arg and displays all values in the states
table from the database hbtn_0e_0_usa where name matches
the arg
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Connect to ythe Mysql
    server"""
    con_db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            port=3306, passwd=sys.argv[2], db=sys.argv[3])

    cursor = con_db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
            %(name) ORDER BY states.id ASC", {'name': sys.argv[4]})

    states = cursor.fetchall()

    for row in states:
        print(row)
