from flask import Flask, render_template, request
import json

app = Flask(__name__)

likes_names = []


class WordBigerOrHaveBannedCharacters(Exception):
    def __init__(self, likes_names):
        super().__init__(likes_names)
    
    def validationNames(likes_names):
        for name in likes_names:
                if name.isalpha() and len(name)<11:
                    continue
                else:
                    raise WordBigerOrHaveBannedCharacters(likes_names)



@app.route("/", methods=["POST", "GET"])

def homepage():
    if request.method == "POST":
        likes_names.append(request.form['name'])

    return render_template('homepage.html')



@app.route("/likes/")
def likes():
     
    dict_results = {"error": False, "data": 'None', "error_message": 'None'}

    try:
        WordBigerOrHaveBannedCharacters.validationNames(likes_names)

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
        dict_results["data"] = data
        return dict_results

    except WordBigerOrHaveBannedCharacters:
        dict_results["error"] = True
        dict_results["data"] = 'None'
        dict_results["error_message"] = '''Вы использовали имя содержащее не буквенные символы или оно больше 10 символов'''
        return dict_results