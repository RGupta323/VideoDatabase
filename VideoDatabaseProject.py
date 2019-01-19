#Database Project
#For now, creating a database of video links for me to access them

from mysql.connector import connection
from mysql.connector import Error
import MySQLdb

cnx=connection.MySQLConnection(
        host='localhost',
        database='python_db',
        user='root',
        password='Tofu123')
cursor=cnx.cursor()
cursor.execute("SELECT VERSION()")
row=cursor.fetchone()
print("server version: ", row[0])
cursor.close()
cnx.close()
