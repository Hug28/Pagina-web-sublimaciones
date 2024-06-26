import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

database_url=os.getenv("DATABASE_URL")

def get_conn():
      try:
            conn = psycopg2.connect(database_url)
            return conn
      except Exception as e:
            print("error",e)


