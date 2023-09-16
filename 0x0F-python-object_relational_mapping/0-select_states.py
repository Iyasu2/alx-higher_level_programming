#!/usr/bin/python3
import MySQLdb
import sys
'''
this module contains code that
lists all states from a
database
'''


def list_states(username, password, db_name):
    '''
    this method connects to a mysql database
    and lists states
    '''
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(username, password, db_name)
