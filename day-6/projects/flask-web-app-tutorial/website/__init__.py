# This file makes the webite folder a python package

# import flask 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()               #add something to bd..
DB_NAME = "database.db"


# define function 
# __name__ represents the name of the file 
def create_app():
    app = Flask(__name__)
#set up config varible['S'] that encryps the cookies and session data relating to our website 
    app.config['SECRET_KEY'] = 'HBJBFSJKDNKJFD DKLFJKFDNSFD'
    # store db as DBNAME in website directory  
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #tell flask that we have blueprints containing different views for our app
    from .views import views
    from .auth import auth

    

    # register blueprint with flack application 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    return app


    def create_database(app):
        if not path.exists('website/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database')
