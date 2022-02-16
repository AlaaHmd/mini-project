import pymysql
import os
from dotenv import load_dotenv




def connect_to_db():
# Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

# Establish a database connection

    connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

    return connection


