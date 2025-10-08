from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Ciao, Mondo!</h3>"

@app.route("/user/<string:username>/age/<int:age>")
def show_user_profile(username: str, age: int):
    return f"Profilo di {username}<br>age: {age}"

@app.route("/post/<int:post_id>")
def show_post(post_id: int):
    return f"Post #{post_id}"

if __name__ == "__main__":
    # avvia direttamente l'app
    app.run(host="127.0.0.1", port=5000, debug=True)
