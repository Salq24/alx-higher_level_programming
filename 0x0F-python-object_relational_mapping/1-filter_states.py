#!/usr/bin/python3

"""
This lists all states from the
database hbtn_0e_0_usa
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

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY id ASC")

    states = cursor.fetchall()

    for row in states:
        print(row)
