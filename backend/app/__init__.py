from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


class Nomination(db.Model):
    name = db.Column(db.String, primary_key=True)
    pic_path = db.Column(db.String)
    seconded = db.Column(db.Boolean)
    votes = db.Column(db.Integer)

    def __init__(self, name, pic_path='', seconded=False, votes=0):
        self.name = name
        self.pic_path = pic_path
        self.seconded = seconded
        self.votes = votes

db.create_all()

@app.route('/api/nominations/', methods = ['GET', 'POST'])
def nominations():
    if request.method == 'GET':
        return jsonify(Nomination.query.all())
    else:
        data = request.get_json()
        name = data.get.name
        pic_path = data.pic_path
        seconded = data.seconded
        votes = data.votes
        nomination = Nomination(name, pic_path, seconded, votes)
        db.session.add(nomination)
        db.session.commit()
        return 201
