#!/usr/bin/python3

"""
This module connects to a MySQL database
"""

import MySQLdb
import sys


def find_state(username, password, db_name, state_name):
    """
    This module connects to a MySQL database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    find_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
