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
    base_url = 'https://qriusity.com/v1/categories'
    url = "{}/{}/questions?page={}&limit=1".format(
        base_url,
        category_id,
        randint(1, 100)
    )
    r = requests.get(url)
    return render_template('question.html', question=json.loads(r.text)[0])
