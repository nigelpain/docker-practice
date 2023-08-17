from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello_database():
    name = get_name()
    return 'Hello {name}!'.format(name=name)

def get_name():
    conn = psycopg2.connect(host=os.environ['DB_HOST'], port=os.environ['DB_PORT'], dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'])
    cur = conn.cursor()
    cur.execute("SELECT first_name FROM exercise_two WHERE id=1;")
    name = cur.fetchone()[0]
    cur.close()
    conn.close()
    return name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
