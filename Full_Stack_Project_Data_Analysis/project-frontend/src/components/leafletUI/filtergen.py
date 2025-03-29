'''
    filtergen.py
    this file generates all possible combinations of coordinates.
'''
import mysql.connector
import sys

sys.path.insert(1, 'C:/Users/tjgal/Downloads/cmsc447team2project/project-backend')

import FlaskServer

def generate():

    

    return

if __name__ == "__main__":
    # Connect to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cmsc447project"
    )
    
    cur = mydb.cursor(buffered=True)

    crimedata_schema = FlaskServer.CrimeDataSchema()

    print("Fetching all crime data")
    crime_all = FlaskServer.get_crimedata()

    generate()

    cur.close()
    