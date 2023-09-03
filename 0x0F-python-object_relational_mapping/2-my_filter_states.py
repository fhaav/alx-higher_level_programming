#!/usr/bin/python3

"""
This script retrieves and lists all states from the hbtn_0e_0_usa database
and prints them in ascending order by their IDs.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
