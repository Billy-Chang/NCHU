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

def checkRowExists(dbcon, tablename, primary_key):
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
    connection = mysql.connector.connect(host='localhost', database='for_python', user='python', password='python123')
    if connection.is_connected():
        cursor = connection.cursor()
        #test for table existed
        if checkTableExists(connection, "Student_info"):
            SQL = "drop table Student_info;"
            result = cursor.execute(SQL)
            print("The table has already existed, drop table.")
        SQL = "create table Student_info(Name varchar(10), ID varchar(10) primary key, Class_num varchar(1), Score int(3));"
        result = cursor.execute(SQL)
        record = cursor.fetchone()                    
        print("Create table successfully!")
        
        list1=['Amy', '1010001', '1', '87']
        list2=['Billy', '1010002', '1', '85']
        list3=['Cindy', '1010003', '1', '92']
        lists=[list1, list2, list3]
        print(lists)
        for i in range(len(lists)):
            if checkRowExists(connection, "Student_info", lists[i][1]):
                print("Record exists!")
            else:
                SQL = "Insert into Student_info values(\"" + lists[i][0] + " \","+lists[i][1]+",\""+lists[i][2]+"\","+lists[i][3]+");"
                print(SQL)
                result = cursor.execute(SQL)
                connection.commit()
                #record = cursor.fetchone()                    
                print("Insert lists" + str(i) + " into table successfully!")
        
        if checkRowExists(connection,"Student_info",list1[1]):
            print("Record exists!")
        else:
            SQL = "Insert into Student_info values(\"" + list1[0] + "\","+list1[1]+",\""+list1[2]+"\","+list1[3]+");"
            print(SQL)
            result = cursor.execute(SQL)
            connection.commit()
            #record = cursor.fetchone()                    
            print("Insert into table successfully!")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed!")
