from flask import Flask
from . import models
from .models import app

# Connect sqlalchemy to app
models.db.init_app(app)

@app.cli.command()
def init_db():
    models.init_db()