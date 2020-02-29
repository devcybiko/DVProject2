from flask import Flask, jsonify, render_template

### create a flask instance
app = Flask(__name__)

sampleData = [
    {"Sunday": "
### one of your API 
@app.route("/api/weeklydata")
def weeklyData():
    return jsonify(justice_league_members)

@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
