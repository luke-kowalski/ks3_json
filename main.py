from configparser import ConfigParser
import mysql.connector

config = ConfigParser()
config.read('config.ini')

MySql_SERVER = config.get("SERVER_CONN", "MySql_SERVER")
MySql_USERNAME = config.get("SERVER_CONN", "MySql_USERNAME")
MySql_PASSWORD = config.get("SERVER_CONN", "MySql_PASSWORD")
MySql_DATABASE = config.get("SERVER_CONN", "MySql_DATABASE")

JSON_OUTPUT_TARGET = config.get("JSON", "JSON_OUTPUT_TARGET")


def dump_json_from_mysql_to_file():

    try:
        connection = mysql.connector.connect(host=MySql_SERVER,
                                            database=MySql_DATABASE,
                                            user=MySql_USERNAME,
                                            password=MySql_PASSWORD)
                    
    except mysql.connector.Error as e:
        print("Something went wrong:", e)
        
    else:
        mycursor = connection.cursor(dictionary=True)
        mycursor.execute("SELECT o.Symbol, o.JSONObject FROM Objects o WHERE o.Symbol LIKE 'S\_%' limit 2")
        myresult = mycursor.fetchall()
        for data in myresult:
            filename = data['Symbol'] + '.json' 
            with open(JSON_OUTPUT_TARGET + filename, 'w',) as f:
                f.write(data['JSONObject'])
                print(filename)