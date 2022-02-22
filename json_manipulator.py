import os
import json
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

JSON_FROM_MYSQL_OUTPUT_TARGET = config.get("JSON", "JSON_FROM_MYSQL_OUTPUT_TARGET")
JSON_TO_MYSQL_FILE_TARGET = config.get("JSON", "JSON_TO_MYSQL_FILE_TARGET")

directory = os.listdir(JSON_FROM_MYSQL_OUTPUT_TARGET)

for file in directory:
    print(file) 
    
    with open(JSON_FROM_MYSQL_OUTPUT_TARGET + file, 'r', encoding='UTF-8', errors='ignore') as f:
        data = json.load(f)

    for item in data['Variables']:
        if item['Name'] == 'ConnectionLeft' or item['Name'] == 'ConnectionRight':
            item['ValueOptions'] = 'Pawcio'
            item['PictureList'] = 'Grubasek'
            
    with open(JSON_TO_MYSQL_FILE_TARGET + file, 'w') as f:
        json.dump(data, f)