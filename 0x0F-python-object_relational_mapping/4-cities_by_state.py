#!/usr/bin/python3

"""
This script lists all cities from the hbtn_0e_4_usa database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute(
            """SELECT cities.id, cities.name, states.name FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            """
    )

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
