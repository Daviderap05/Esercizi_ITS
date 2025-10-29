from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Ciao, Mondo!</h3>"

@app.route("/user/<string:name>")
def show_user_name(name: str):
    return f"<p>Benvenuto/a,  {name.capitalize()}!</p>"

@app.route("/square/<int:n>")
def square(n: int):
    return f"<p>{n}^2 = {n ** 2}</p>"

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    return f"<p>{a} + {b} = {a + b}</p>"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)