import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base

# 環境変数を読み込む
load_dotenv()

# 環境変数から接続情報を取得
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_SSL_CA = os.getenv('DB_SSL_CA')

config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': DB_SSL_CA,
}

Base = declarative_base()

def get_db_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
           print("Successfully connected to the database") 
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
