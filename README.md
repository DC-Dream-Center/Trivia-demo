# Simple Trivia web app

Written in [Flask](http://flask.pocoo.org/), a Python micro framework

Using the [Qriusity API](https://qriusity.com/) allow a user to select a category, and answer trivia questions.

### To run locally
clone this project
```
git clone https://github.com/DC-Dream-Center/Trivia-demo.git
```
Navigate to the new directory
```
cd Trivia-demo
```
Install python requirements using [pip](https://pip.pypa.io/en/stable/)
```
pip install -r requirements.txt
```
Run the application locally
```
FLASK_APP=trivia.py flask run
```
Once running, open your browser and go to `localhost:5000` in your address bar
