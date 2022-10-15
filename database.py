""" Creation of the database to store new found cars"""

import sqlite3

conn = sqlite3.connect("name_of_the_database.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS auto")
cursor.execute("""
  CREATE TABLE IF NOT EXISTS auto(
  name char(50) PRIMARY KEY, 
  price integer, 
  link char(100)
  )
""")
