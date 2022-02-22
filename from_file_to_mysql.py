import os
from configparser import ConfigParser
import mysql.connector

config = ConfigParser()
config.read("config.ini")

MySql_SERVER = config.get("SERVER_CONN", "MySql_SERVER")
MySql_USERNAME = config.get("SERVER_CONN", "MySql_USERNAME")
MySql_PASSWORD = config.get("SERVER_CONN", "MySql_PASSWORD")
MySql_DATABASE = config.get("SERVER_CONN", "MySql_DATABASE")

JSON_TO_MYSQL_FILE_TARGET = config.get("JSON", "JSON_TO_MYSQL_FILE_TARGET")

directory = os.listdir(JSON_TO_MYSQL_FILE_TARGET)


def from_file_to_mysql():

    rows_affected = 0

    try:
        connection = mysql.connector.connect(
            host=MySql_SERVER,
            database=MySql_DATABASE,
            user=MySql_USERNAME,
            password=MySql_PASSWORD,
        )
    except mysql.connector.Error as e:
        print("Something went wrong:", e)
    else:
        for file in directory:
            with open(
                JSON_TO_MYSQL_FILE_TARGET + file, "r", encoding="UTF-8", errors="ignore"
            ) as f:
                data = f.read()

                mycursor = connection.cursor()
                sql_symbol = file.split(".", 1)[0]

                sql = "UPDATE objects SET JSONObject = %s WHERE symbol = %s"
                val = (data, sql_symbol)
                print(sql_symbol)
                mycursor.execute(sql, val)
                connection.commit()
                rows_affected += 1

        print(rows_affected, "record(s) affected")


from_file_to_mysql()
