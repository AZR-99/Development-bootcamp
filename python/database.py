import mysql.connector

#config= {
#"host": "localhost", 
#"user": "root" , 
#"password": "hello99"
#"database": "test_db"
#}
#db_connection = mysql.connector.connect

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hello99"
)

cursor=db_connection.cursor()
create_database_query = "CREATE DATABASE test_db"
cursor.execute(create_database_query)

#commit the changes 
db_connection.commit()

#close the cursor and the connection 
cursor.close()
db_connection.close()
print("Database created")