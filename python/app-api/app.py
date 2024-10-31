
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import cross_origin
import mysql.connector
app = Flask(__name__)
# Database connection configuration
def create_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'hello99',
        database = 'e_careers'
    )
    return connection    
#mysql = MySQL(app)
@app.route('/data', methods=['GET'])
@cross_origin(origins='*')
def get_data():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT * from employee''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def post_data():
    #cur = mysql.connection.cursor()
    connection = create_connection()
    cur = connection.cursor()
    id = request.json['id']
    name = request.json['emp_name']
    dept = request.json['emp_dept']
    salary = request.json['emp_sal']
    cur.execute('''INSERT INTO employee (emp_id, emp_name, emp_dept, emp_salary) VALUES(%s, %s, %s, %s)''', (id, name, dept, salary))
    #mysql.connection.commit()
    cur.close()
    return jsonify({'message':'Data inserted successfully'})

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from employee where emp_id = %s''', (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/data/<int:id>', methods=['PUT'])
def update_data_by_id(id):
    cur = mysql.connection.cursor()
    name = request.json['emp_name']
    dept = request.json['emp_dept']
    cur.execute('''UPDATE employee SET emp_name = %s, emp_dept = %s WHERE emp_id = %s''', (name, dept, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message':'Data updated successfully'})

if __name__ == '__main__':
    app.run(port=5002) 
