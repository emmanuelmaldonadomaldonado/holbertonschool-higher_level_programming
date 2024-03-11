#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument in a safe way
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = '{}';".format(sys.argv[4]))
        states = cur.fetchall()

        print(", ".join([state[1] for state in states]))
