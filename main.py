from configparser import ConfigParser
import mysql.connector
from mysql.connector import Error

config = ConfigParser()
config.read('config.ini')

MySql_SERVER = config.get("SERVER_CONN", "MySql_SERVER")
MySql_USERNAME = config.get("SERVER_CONN", "MySql_USERNAME")
MySql_PASSWORD = config.get("SERVER_CONN", "MySql_PASSWORD")
MySql_DATABASE = config.get("SERVER_CONN", "MySql_DATABASE")



try:
    connection = mysql.connector.connect(host=MySql_SERVER,
                                         database=MySql_DATABASE,
                                         user=MySql_USERNAME,
                                         password=MySql_PASSWORD)


    mycursor = connection.cursor()
    mycursor.execute("SELECT o.Symbol FROM Objects o WHERE o.Symbol LIKE 'S\_%'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        # with open(x[0] + '.json', 'w',) as f:
        #     f.write(x[1])
                
except Error as e:
    print("Error while connecting to MySQL", e)
    
finally:
    mycursor.close()
    connection.close()