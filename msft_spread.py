# import necessary tools
import sqlite3
import csv

# create connection and sets up cursor tool
conn = sqlite3.connect('msft_high_lowdb.sqlite')
cur = conn.cursor()

# clears SQL of any tables with same name
# sets up desired table w/ correct info
cur.executescript('''
DROP TABLE IF EXISTS MSFT_HL;

CREATE TABLE MSFT_HL(
date DATE,
low REAL,
high REAL,
spread REAL)''')

# sets up Dict Reader to read through file by column name and not by item in a list
# find/calculate correct variables
# send info to new table
fh = input("Enter MSFT file:")
with open(fh, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = row['date']
        low = float(row['low'])
        high = float(row['high'])
        spread = ((high-low)/low)
        cur.execute("INSERT INTO MSFT_HL (date,low,high,spread) VALUES (?,?,?,?)", (date, low, high, spread))

# filter through new table and pick what I want to eventually print
query = "SELECT date,spread from MSFT_HL ORDER BY spread DESC LIMIT 10"
cur.execute(query)
high_low_spread = cur.fetchall()

# sets up formatting for how I want info to appear in python when printed
print(f"{'date': <20} | {'spread': <20}")
print('-'*40)
for date, spread in high_low_spread:
    print(f"{date:<20} | {spread:<20.2%}")

conn.commit()
conn.close()
