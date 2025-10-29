from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return f"""
        <h1>Home</h1>
        <a href='{url_for('about')}'>About</a><br>
        <a href='{url_for('users')}'>Utenti</a><br>
        <a href='{url_for('posts')}'>Post</a><br>
        <a href='{url_for('user_profile', username="alice")}'>Profilo Alice</a><br>
        <a href='{url_for('post_detail', id=1)}'>Post 1</a>
    """


@app.route('/about')
def about():
    return "<h1>Pagina About</h1><a href='/'>Torna alla home</a>"


@app.route('/users')
def users():
    users: list[str] = ['alice', 'bob', 'carol']
    links: str = "".join(f"<li><a href='{url_for('user_profile', username=u)}'>{u}</a></li>" for u in users)
    return f"<h1>Utenti</h1><ul>{links}</ul><a href='/'>Home</a>"


@app.route('/user/<username>')
def user_profile(username: str):
    return f"<h1>Profilo di {username}</h1><a href='{url_for('users')}'>Torna agli utenti</a>"


@app.route('/posts')
def posts():
    ids: list[int] = [1, 2, 3]
    links: str = "".join(f"<li><a href='{url_for('post_detail', id=i)}'>Post {i}</a></li>" for i in ids)
    return f"<h1>Elenco post</h1><ul>{links}</ul><a href='/'>Home</a>"


@app.route('/post/<int:id>')
def post_detail(id: int):
    return f"<h1>Post {id}</h1><p>Contenuto del post {id}.</p><a href='{url_for('posts')}'>Torna ai post</a>"


if __name__ == "__main__":
    app.run(debug=True)