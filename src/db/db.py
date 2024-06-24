import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()
database=os.getenv("DATA_BASE")
user=os.getenv("USER")
password=os.getenv("PASSWORD")

def get_conn():
      try:
            conn = psycopg2.connect(database=database, user=user, password=password)
            return conn
      except Exception as e:
            print("error",e)