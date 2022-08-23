from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static') # instantiation application

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

app.run(debug=True) # démarrage de l’application