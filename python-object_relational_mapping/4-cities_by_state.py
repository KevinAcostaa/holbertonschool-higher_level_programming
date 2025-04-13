#!/usr/bin/python3
"""
This module connects to a MySQL database
"""

import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Connect to a MySQL database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
