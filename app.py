import json
from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Load database configuration from JSON file
def load_db_config():
    with open('db_config.json', 'r') as file:
        config = json.load(file)
    return config

# Database connection
def get_db_connection():
    config = load_db_config()
    connection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password']
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def get_databases():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SHOW DATABASES')
    databases = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', databases=[db[0] for db in databases])

@app.route('/database/<dbname>')
def database(dbname):
    # You can customize this part to display tables or contents of the selected database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f'SHOW TABLES IN `{dbname}`')  # Example query to show tables in the selected database
    tables = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('database.html', dbname=dbname, tables=[table[0] for table in tables])

@app.route('/database/<dbname>/table/<tablename>')
def table_contents(dbname, tablename):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM `{dbname}`.`{tablename}`')  # Fetch all rows from the selected table
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('table.html', dbname=dbname, tablename=tablename, rows=rows)






if __name__ == '__main__':
    app.run(debug=True)