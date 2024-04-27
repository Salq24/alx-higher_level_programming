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

    cursor.execute("""SELECT cities.id, cities.name FROM\
            cities JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %(state_name)s\
            ORDER BY cities.id ASC""", {'state_name': sys.argv[4]})

    cities = cursor.fetchall()

    if cities is not None:
        print(", ".join([city[1] for city in cities]))
