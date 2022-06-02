from flask import Flask 
app = Flask (__name__) 

@app.route("/")
def homepage(): 
	return 'Welcome to My Portfolio!'

@app.route("/aboutme")
def aboutMe(): 
	return 'Learn about me'

@app.route("/experience")
def workExp(): 
	return 'Here are some things I've worked on'

@app.route("/hobbies")
def hobbies(): 
	return 'Some things I like to do'

@app.route("/education")
def education(): 
	return 'Education:' 

@app.route("/myMap")
def myMap(): 
	return 'Some places I've been to' 
