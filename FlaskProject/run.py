import os
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello():
    all_things = ['Piano', 'Guitar', 'Violin', 'Flute']
    name = 'Rika!'
    print(request.form)
    if request.form.get('StringToConvert'):
        if 'tl' in request.form:
            string_to_convert = str(request.form['StringToConvert']).lower()
        else:
            string_to_convert = str(request.form['StringToConvert']).upper()
    else:
        string_to_convert = None
    return render_template('index.html', name=name, stc=string_to_convert, items=all_things)

@app.route("/test")
def test():
    return render_template('test.html')



# For loading css every time, not using the one in cache

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
