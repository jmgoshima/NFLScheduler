import sqlite3
import pandas as pd
from datetime import datetime

db_file = "nfl.db"
csv_file = "data/2024_scores.csv"

df = pd.read_csv(csv_file)

