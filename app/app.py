import os
import datetime
from flask import Flask, render_template, request
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from peewee import *
from flask import Response
import re

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    #creates database 
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
    )

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

@app.route("/timeline")
def timeline(): 
	posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
	return render_template('timeline.html', title="Timeline", posts=posts)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    try:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content'] 
        if content == "":
            # page = render_template('error.html', title="Invalid content")
            return Response(
            "Invalid content",
            status=400,
            )
        elif name == "":
            # page = render_template('error.html', title="Invalid name")
            return Response(
            "Invalid name",
            status=400,
            )
        else:
            if(re.fullmatch(regex, email)):
                timeline_post = TimelinePost.create(name=name, email=email, content=content)
                return model_to_dict(timeline_post)
            else:
                # page = render_template('error.html', title="Invalid email")
                return Response(
                "Invalid email",
                status=400,
                )
    except:
        # page = render_template('error.html', title="Invalid name")
	    return Response("Invalid name", status=400)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post(): 
	return { 
		'timeline_posts': [
			model_to_dict(p)
			for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
		]
	}

# @app.route('/api/timeline_post/<int:nid>', methods=['DELETE'])
# def delete_time_line_post(nid):
#     try:
#         obj=TimelinePost.get(TimelinePost.id==nid)
#         obj.delete_instance()
#         return get_time_line_post()
#         # return "Done"
#     except TypeError:
#         from traceback import format_exec
#         print(format_exec())

@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
#     if not testing: mydb.connect()
    post_to_delete = TimelinePost.get(TimelinePost.id == id)
    deleted_post = model_to_dict(post_to_delete)
    post_to_delete.delete_instance()
#     if not testing: mydb.close()

    return deleted_post
    
# @app.route("/api/timeline_post/<id>", methods=['DELETE'])
# def delete_timeline_post(id):
#     toDelete = TimelinePost.query.get(id)
#     mydb.session.delete(toDelete)
#     mydb.session.commit()

#     return { 
# 		'timeline_posts': [
# 			model_to_dict(p)
# 			for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
# 		]
# 	}

#     # return "Post was successfully deleted"

# @app.route('/api/timeline_post/<int:nid>', methods=['DELETE'])
# def delete_time_line_post(nid): 
# 	post_to_delete = TimelinePost.delete().where(TimelinePost.id == nid)
# 	post_to_delete.execute()
# 	print("Deleted successfully")
# 	# return { 
# 	# 	'timeline_posts': [
# 	# 		model_to_dict(p)
# 	# 		for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
# 	# 	]
# 	# }


