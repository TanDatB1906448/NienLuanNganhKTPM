from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def homePage():
    return render_template("index.html")

@views.route("/flowers")
def flowersPage():
    return render_template("flowers.html")

@views.route("/contact")
def contactPage():
    return render_template("contact.html")

@views.route("/recognize")
def recognitionPage():
    return render_template("recognize.html")
