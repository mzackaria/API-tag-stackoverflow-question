# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:34:54 2018

@author: zakis
"""
from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .get_result import result
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

# Create database connection object
db = SQLAlchemy(app)


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ident = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    cluster = db.Column(db.String(200), nullable=False)

    def __init__(self, ident, cluster, title):
        self.ident = ident
        self.title = title
        self.cluster = cluster
    
    def dict_(self):
        return {"id":self.ident,"title":self.title}

def init_db():
    db.drop_all()
    db.create_all()
    for i in range(0,len(result.values)):
        ident = result.iloc[i,0].astype(str)
        cluster = result.iloc[i,1].astype(str)
        title = result.iloc[i,2].replace(u"\u00A0", "")
        db.session.add(Film(ident,cluster,title))
    db.session.commit()
    lg.warning('Database initialized!')
     
    
@app.route('/recommend/<id_film>', methods = ['GET'])
def index(id_film):
        film = Film.query.filter_by(ident=str(id_film)).first()
        if film is None:
            return "Wrong id > " + str(id_film)
        same_films = Film.query.filter_by(cluster=film.cluster).all()
        same_films.remove(film)
        result = []
        for i in range(0,5):
            f = random.choice(same_films)
            same_films.remove(f)
            result.append(f.dict_())
        return  jsonify({"film":film.dict_(), "results":result})


@app.route('/recommend/')
def ind():
        return "hello"
    
if __name__ == "__main__":
        app.run()