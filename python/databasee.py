import mysql.connector, db_config
config = db_config.config
try: 
    db_connection = mysql.connector.connect(**config)
    cursor=db_connection.cursor()
    sql_select_query = "select * from employee"
    cursor.execute(sql_select_query, prams=[101])
    data = cursor.fetchall()
    for row in data: 
        print('EmpId= ',row[0],)
        print('EmpName= ',row[1],)
        print('EmpDept= ',row[2],)
        print('EmpSalary=',row[3],)
        print("--------------------")

        db_connection.commit()
except mysql.connector.Error as e: 
    print("Error reading data")
finally: 
    if db_connection.is.connected():
    db_connection.close
    cursor.close()              