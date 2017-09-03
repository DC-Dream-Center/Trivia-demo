from flask import Flask
from flask import render_template
import json
from random import randint
import requests
app = Flask(__name__)


@app.route("/")
def categories():
    r = requests.get('https://qriusity.com/v1/categories')
    return render_template('categories.html', categories=json.loads(r.text))


@app.route("/question/<category_id>")
def question(category_id):
    url = "https://qriusity.com/v1/categories/{}/questions?page={}&limit=1".format(category_id,randint(1, 100))
    r = requests.get(url)
    return render_template('question.html', question=json.loads(r.text)[0])
