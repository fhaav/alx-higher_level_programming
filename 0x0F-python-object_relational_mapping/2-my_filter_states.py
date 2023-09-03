#!/usr/bin/python3

"""
This script retrieves and lists all states from the hbtn_0e_0_usa database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_prefix = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
ii
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
