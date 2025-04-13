#!/usr/bin/python3
"""
    Connect to a MySQL database and list
    all states with names starting with 'N'.
"""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Connect to a MySQL database and list
    all states with names starting with 'N'.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
