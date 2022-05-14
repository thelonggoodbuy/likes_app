from flask import Flask, render_template, url_for

app = Flask(__name__)

# homepage with post
@app.route("/", methods=['GET'])
def homepage():
    return render_template('homepage.html')



#page for likes
@app.route("/likes")
def likes():
    return "<p>There will be dictionary with likes</p>"