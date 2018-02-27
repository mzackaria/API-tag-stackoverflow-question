from flask import Flask

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def ind():
    return 'Hello p'
    
@app.route('/recommend/<id_film>')
def index(id_film):
        return id_film

if __name__ == "__main__":
        app.run()