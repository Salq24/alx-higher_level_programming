#!/usr/bin/python3

"""
This lists all cities from the database
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

    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
            cities JOIN states ON cities.state_id = states.id ORDER\
            BY cities.id ASC")

    cities = cursor.fetchall()

    for row in cities:
        print(row)
