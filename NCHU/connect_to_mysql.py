import mysql.connector
from mysql.connector import Error

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

try:
    connection = mysql.connector.connect(host='localhost',database='for_python',user='python',password='python123')
    if connection.is_connected():
        cursor = connection.cursor()
        #test for table existed
        if checkTableExists(connection, 
                            "Student_info"):
            SQL = "drop table Student_info;"
            result = cursor.execute(SQL)
            print("drop table")
        SQL = "create table Student_info(name varchar(10), ID varchar(10) primary key, Class_name varchar(1), Score int(3));"
        result = cursor.execute(SQL)
        record = cursor.fetchone()                    
        print("Create table successfully!")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed!")

    