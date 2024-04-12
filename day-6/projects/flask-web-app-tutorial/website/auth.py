# from flask import Blueprint, render_template, request
# # from flask import render_template 

# # This file is a blueprint of our app/It has routes
# auth = Blueprint('auth', __name__)

# # define auth
# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     # get information sent in form
#     # data = request.form
#     # print(data)
#     if request.method == "POST":
#         email = request.form.get('email')
#         firstName = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         if len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
# # add user to db
#     return render_template("login.html", boolean=True)

# # define auth
# @auth.route('/logout')
# def logout():
#     return "<p>Logout</p>"

# # define auth
# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     return render_template("sign_up.html")

# ///////////////////////////////////////////////////////////////////////////////////////////////

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__)
from . import db

import hashlib

# Create a new hashlib object for SHA-256
hash_object = hashlib.sha256()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Hash the password before storing it in the database
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
            # Create a new user object and add it to the database session
            new_user = User(email=email, first_name=first_name, password=hashed_password)
            db.session.add(new_user)
            # Commit the changes to the database
            db.session.commit()
            flash('Account created successfully!', category='success')
            # Redirect the user to the home page after successful registration
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")