from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'money_db')
# an example of running a query
print mysql.query_db("SELECT * FROM debtors")
app.run(debug=True)