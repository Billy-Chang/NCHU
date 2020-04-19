import mysql.connector
from mysql.connector import Error

def checkRowExists(dbcon, tablename,primary_key):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM """+tablename+"""
        WHERE ID="""+primary_key)
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
        list1=input().split()
        print(list1)
        if checkRowExists(connection,"Student_info",list1[1]):
            SQL = """
                delete from Student_info
                Where `ID` ="""+ list1[1]+ """;""" 
            result = cursor.execute(SQL)
            connection.commit()
        SQL = "Insert into Student_info values(\"" + list1[0] + "\","+list1[1]+",\""+list1[2]+"\","+list1[3]+");"
        print(SQL)
        result = cursor.execute(SQL)
        connection.commit()
        #record = cursor.fetchone()                    
        print(  "Insert into table successfully!")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

    