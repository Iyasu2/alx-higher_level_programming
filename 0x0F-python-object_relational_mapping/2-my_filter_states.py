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

    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{}' "
                "ORDER BY id ASC".format(state_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
