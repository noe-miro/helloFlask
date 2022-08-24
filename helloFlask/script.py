from flask import Flask, render_template, request, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_url_path='/static') # instantiation application
app.config["SECRET_KEY"] = str(os.urandom(3).hex()) # for forms

UPLOAD_FOLDER = './helloFlask/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_PATH'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = 6291456 # max upload size in bytes

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# class MyForm(FlaskForm):
#     myStringField("My Text")
#     mySubmitField("Submit My Form")
messages = [] # for the form

@app.route("/")
def home(name='Noemi'): # association d’une route (URL) avec la fonction ‘home()’
    # return "<p>Bienvenue chez moi</p>"  # on renvoie une chaîne de caractères
    return render_template('index.html', name=name)

@app.route("/cat")    #specifies URL
def cat(): # This function name is the variable called in _navigation.html
    return render_template('cat.html')

@app.route("/more_cats")    #specifies URL
def more_cats(): # This function name is the variable called in _navigation.html
    return render_template('more_cats.html')

@app.route("/AI")    #specifies URL
def AI(): # This function name is the variable called in _navigation.html
    return render_template('AI.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('more_cats'))

    return render_template('create.html')

@app.route('/test_upload')
def upload_form():
   return render_template('test_upload.html')

@app.route('/uploader/', methods=('GET', 'POST'))
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(f.filename)))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True) # démarrage de l’application