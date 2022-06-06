from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/")
def homepage(): 
	# acts as a homepage and an "About Me" page
	return render_template("homepage.html", title="Maisha's Portfolio")

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

if __name__ == "__main__": 
	app.run(debug=True)