from flask import Flask, jsonify, render_template

### create a flask instance
app = Flask(__name__)

sampleData = [
    {"day": "Sunday", "value": 15339},
    {"day": "Monday", "value": 21345},
    {"day": "Tuesday", "value": 18483},
    {"day": "Wednesday", "value": 24003},
    {"day": "Thursday", "value": 23489},
    {"day": "Friday", "value": 24092},
    {"day": "Saturday", "value": 12034}
]
    
### one of your APIs
@app.route("/api/weeklydata")
def weeklyData():
    return jsonify(sampleData)

@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
