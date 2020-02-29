from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/api/justice-league")
def justice_league():
    return jsonify(justice_league_members)

@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
