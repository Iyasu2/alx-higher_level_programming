#!/usr/bin/python3
'''
this module contains code that
lists all states from a
database
'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    state_name = sys.argv[4]

    cur = db.cursor()

    query = '''SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC'''

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
