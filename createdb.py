import sqlite3
import pandas as pd
from datetime import datetime

db_file = "nfl.db"
csv_file = "data/2024_scores.csv"

df = pd.read_csv(csv_file)

# Print controls: debug (self-explanatory)
debug = False

# Attempts to create a database
try:
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	print("Database bookstore.db formed.")
except:
	print("Database bookstore.db not formed")

if debug:
	print("Database columns: ")
	print(df.columns)

# Create tables
cursor.execute(f"""
	CREATE TABLE IF NOT EXISTS CONFERENCE
(
	ConferenceID	INT		        NOT NULL,
	Name            VARCHAR(30)     NOT NULL,     
	PRIMARY KEY(ConferenceID)
);
""")

cursor.execute(f"""
	CREATE TABLE IF NOT EXISTS DIVISION
(
	DivisionID	    INT     		NOT NULL,
	Name            VARCHAR(30)     NOT NULL,   
    ConferenceID    INT             NOT NULL,
	PRIMARY KEY(DivisionID),
	FOREIGN KEY(ConferenceID) REFERENCES CUSTOMER(ConferenceID)
);
""")

cursor.execute(f"""
	CREATE TABLE IF NOT EXISTS TEAM
(
	TeamID	            INT     		NOT NULL,
	City                VARCHAR(30)     NOT NULL,   
    Name                VARCHAR(30)     NOT NULL, 
	Abbreviation        VARCHAR(30)     NOT NULL,
    DivisionID          INT             NOT NULL,
	PRIMARY KEY(TeamID),
	FOREIGN KEY(DivisionID) REFERENCES CUSTOMER(DivisionID)
);
""")




# Close the connection
conn.close()
