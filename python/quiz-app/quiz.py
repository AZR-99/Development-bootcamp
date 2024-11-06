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
    cur.execute("select id, title, description from quizzes")
    quizzes = cur.fetchall() 
    cur.close()
    connection.close()
    return jsonify(quizzes)

@app.route('/quizzes/<int:quiz_id>/questions', methods=['GET'])
def get_questions(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute("select id, question_text from questions where quiz_id = %s", (quiz_id,))
    questions = cur.fetchall()  

    for question in questions:
        question_id = question['id']
        cur.execute("select id, choice_text, is_correct from choices where question_id = %s", (question_id,))
        question['choices'] = cur.fetchall()  

    cur.close()
    connection.close()
    return jsonify(questions)

@app.route('/api/submit', methods=['POST'])
def post_data():
    data = request.get_json()  
    answers = data.get('answers', [])  
    score = 0  

    # connecting to database
    connection = create_connection()
    cur = connection.cursor()

    for answer in answers:
        question_id = answer['question_id']  # gets the ID
        choice_id = answer['choice_id']  # # gets the ID

        # checks to see if the choice is right or wrong
        cur.execute("select is_correct FROM choices where id = %s and question_id = %s", (choice_id, question_id))
        result = cur.fetchone()  # gets the result 
        if result and result[0]:  # if its correct score will increase
            score += 1

    cur.close()
    connection.close()

    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(port=5003) 

