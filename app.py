from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():

    return render_template("home.html",title ="Homepage")

@app.route("/about")
def about():

    return render_template("about.html",title= "About")


@app.route("/contact")
def contact():

    return render_template("contact.html",title="Contact")

@app.route("/gallery")
def gallery():

    return render_template("gallery.html",title="Gallery")

@app.route("/openAI")
def openAI():
    return render_template("openAI.html",title="OpenAI")
    
   

