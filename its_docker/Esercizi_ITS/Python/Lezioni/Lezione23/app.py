from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return '<h3>Ciao, Mondo!<h3>'

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int):
    return f'Profilo di {username}\nage: {age}'

@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    return f'Profilo di {post_id}'