from flask import Flask, render_template
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'arizona'

mysql = MySQL(app)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/roster")
def roster():
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM arizona_roster")
	fetchdata = cursor.fetchall()
	cursor.close()
	return render_template("roster.html", data = fetchdata)

if __name__ == "__main__":
    app.run(debug=True)
