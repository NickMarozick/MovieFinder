'''
Contributors: Nick Marozick, Alex Marozick
'''

from flask import Flask, render_template, url_for, request, redirect, abort, flash, jsonify, session, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/GetByTitle')
def getByTitle():
    return render_template("getByTitle.html")

@app.route('/GetByGenre')
def getByGenre():
    return render_template("getByGenre.html")

@app.route('/GetSimiliar')
def getSimiliar():
    return render_template("getSimiliar.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=False)
