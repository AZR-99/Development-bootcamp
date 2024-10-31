from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import cross_origin
import mysql.connector
app = Flask(__name__)

def create_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'hello99',
        database = 'online_quiz'
    )
    return connection

@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute("SELECT id, title, description from quizzes")
    questions = cur.fetchall()
    cur.close()
    return jsonify(quizzes)

def get_questions(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute("SELECT id, choice_text from questions where quiz_id %s", (quiz_id,))
    questions = cur.fetchall()