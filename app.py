from flask import Flask, render_template, url_for, request

app = Flask(__name__)

likes_names = []


# homepage with post
@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        print(request.form['name'])
        likes_names.append(request.form['name'])
        # print(likesname)
    return render_template('homepage.html')



#page for likes
@app.route("/likes")
def likes():

    upper_names = [name.title() for name in likes_names]
    tuple_names = tuple(upper_names)

    print('This is secont function:', tuple_names)
    if len(tuple_names) == 0:
        return "Это никоему не нравиться"
    elif len(tuple_names) == 1:
        return "{0} лайкнул это".format(*tuple_names)
    elif len(tuple_names) == 2:
        return "{0} и {1} лайкнули это".format(*tuple_names)
    elif len(tuple_names) == 3:
        return "{0}, {1} и {2} лайкнули это".format(*tuple_names)
    else:
        return "{0} и {1} и еще {2} лайкнули это".format(tuple_names[0],\
             tuple_names[1], len(upper_names[2:]))




# 0.5 + 1
