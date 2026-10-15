import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur=conn.cursor()
  #creating the table 
cur.execute(''' 
CREATE TABLE users(
  id integer primary key,
  name text not null,
  email text not null unique,
  signup_date date default current_date
  );
  ''')

cur.execute(''' 
alter table users add column phone_number text;''') 
  #inseri the data into the table
cur.execute("""
    INSERT INTO users (name, email)
    VALUES 
        ('Sofia Ramirez', 'sofia.ramirez@example.com'),
        ('Devon Blake', 'devon.blake@example.com');
""")

conn.commit()
cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())
 #updating the users
cur.execute("""
    UPDATE users
    SET email = 'devon.blake@newdomain.com'
    WHERE email = 'devon.blake@example.com';
""")

conn.commit()

conn.close()