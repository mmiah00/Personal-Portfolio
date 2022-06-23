import os
import datetime
from flask import Flask, render_template, request
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from peewee import *

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"),host=os.getenv("MYSQL_HOST"), port=3306)

print(mydb)

class TimelinePost(Model): 
	name = CharField()
	email = CharField()
	content = TextField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta: 
		database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route("/")
def index(): 
	# acts as a homepage and an "About Me" page
	return render_template("index.html", title="Maisha's Portfolio")

@app.route("/experience")
def workExp(): 
	return render_template("experience.html", title="Work Experience")

@app.route("/hobbies")
def hobbies(): 
	return render_template("hobbies.html", title="Hobbies")

@app.route("/education")
def education(): 
	return render_template("education.html", title="Education") 

@app.route("/myMap")
def myMap(): 
	return render_template("map.html", title="Map") 

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post(): 
	name = request.form['name']
	email = request.form['email']
	content = request.form['content']
	timeline_post = TimelinePost.create(name=name, email=email, content=content)

	return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post(): 
	return { 
		'timeline_posts': [
			model_to_dict(p)
			for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
		]
	}



# from flask import Flask, render_template
# app = Flask(__name__) 

# @app.route("/")
# def index(): 
# 	# acts as a homepage and an "About Me" page
# 	return render_template("index.html", title="Maisha's Portfolio")

# @app.route("/experience")
# def workExp(): 
# 	return render_template("experience.html", title="Work Experience")

# @app.route("/hobbies")
# def hobbies(): 
# 	return render_template("hobbies.html", title="Hobbies")

# @app.route("/education")
# def education(): 
# 	return render_template("education.html", title="Education") 

# @app.route("/myMap")
# def myMap(): 
# 	return render_template("map.html", title="Map") 

# if __name__ == "__main__": 
# 	app.run(debug=True)