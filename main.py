from flask import Flask, render_template
# venv oluşturduktan sonra terminale yazılması gereken
# export FLASK_ENV=development
# export FLASK_APP=main.py


app = Flask(__name__)



#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


