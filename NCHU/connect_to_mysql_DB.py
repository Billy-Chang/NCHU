# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:14:10 2020

@author: jains
"""

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='for_python',
        user='python',
        password='python123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version",db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()            
        print("You're connected to database:", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")