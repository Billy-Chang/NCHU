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

def search_table(dbcon, tablename,feature,value):
    dbcur = dbcon.cursor()
    SQL1="""Select * from """+tablename+""" 
          where """ + feature +""" = \"
          """ + value+"""\";"""
    dbcur.execute(SQL1)
    record = cursor.fetchall()
    return record

try:
    connection = mysql.connector.connect(host='localhost',database='for_python',user='python',password='python123')
    tablename1=input("Please enter the table name>")
    if connection.is_connected():
        cursor = connection.cursor()
        #test for table existed
        if checkTableExists(connection,tablename1):
            feature=input("Please enter the feature name>")
            value=input("Please enter the feature value>")
            record=search_table(connection, 
                         tablename1, 
                         feature, value)
            for i in record:
                print(i)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

    