from flask import Flask, render_template, url_for, request

app = Flask(__name__)

likes_names = []
likes_url = ",".join(likes_names)


@app.route("/", methods=["POST", "GET"])

def homepage():
    if request.method == "POST":
        print(request.form['name'])
        likes_names.append(request.form['name'])

    return render_template('homepage.html')



@app.route("/likes/")
# @app.route("/likes")
def likes():
    
    print(likes_names)

    for name in likes_names:
        if name.isalpha() and len(name)<11:
            continue
        else:
            data = 'ERROR'
            return data

    upper_names = [name.title() for name in likes_names]

    tuple_names = tuple(upper_names)

    if len(tuple_names) == 0:
        data = "Это никоему не нравиться"
    elif len(tuple_names) == 1:
        data = "{0} лайкнул это".format(*tuple_names)
    elif len(tuple_names) == 2:
        data = "{0} и {1} лайкнули это".format(*tuple_names)
    elif len(tuple_names) == 3:
        data = "{0}, {1} и {2} лайкнули это".format(*tuple_names)
    else:
        data = "{0} и {1} и еще {2} лайкнули это".format(tuple_names[0],\
            tuple_names[1], len(upper_names[2:]))
    return data




# 0.5 + 1 + 1.5 +1.5

# 5. - воскресенье


# 45min