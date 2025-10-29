from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Ciao, Mondo!</h3>"

@app.route("/about")
def show_info (info: str = "informazioni..."):
    return f"<p>Ecco le info: {info}</p>"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)