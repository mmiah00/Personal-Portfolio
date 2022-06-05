from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/")
def homepage(): 
	# acts as a homepage and an "About Me" page
	return render_template("homepage.html")

@app.route("/experience")
def workExp(): 
	return render_template("experience.html") 

@app.route("/hobbies")
def hobbies(): 
	return render_template("hobbies.html")

@app.route("/education")
def education(): 
	return render_template("education.html") 

@app.route("/myMap")
def myMap(): 
	return render_template("map.html") 

if __name__ == "__main__": 
	app.run(debug=True)