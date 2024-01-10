import psycopg2
import os
from dotenv import load_dotenv
psycopg2.connect()
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS laptop_data(id integer PRIMARY KEY,
model text,
current_price real,
processor test,
os text,
praphics text,
memory text,
storage text,
display text
)""")
conn.commit()
conn.close()
cursor.close()
