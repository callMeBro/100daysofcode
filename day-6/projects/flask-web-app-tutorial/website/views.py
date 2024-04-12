# store routes for website

# import flask, render_template
from flask import Blueprint, render_template

# This file is a blueprint of our app/It has routes
views = Blueprint('views', __name__)


# define view
@views.route('/')
def home():
    return render_template('home.html')

