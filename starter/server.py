from flask import Flask, jsonify, render_template

### create a flask instance
app = Flask(__name__)

someWeeklyPerformanceData = [
    {"day": "Sunday", "value": 15339},
    {"day": "Monday", "value": 21345},
    {"day": "Tuesday", "value": 18483},
    {"day": "Wednesday", "value": 24003},
    {"day": "Thursday", "value": 23489},
    {"day": "Friday", "value": 24092},
    {"day": "Saturday", "value": 12034}
]

theDataForSalaries = [
        {'Salaries':1200000, 'Office':20000, 'Merchandise':80000, 'Legal':2000, 'Total':12120000},
        {'Salaries':1300000, 'Office':20000, 'Merchandise':70000, 'Legal':2000, 'Total'},
        {'Salaries', 'Office', 'Merchandise', 'Legal', 'Total'},
        {'Salaries', 'Office', 'Merchandise', 'Legal', 'Total'},
        [, , , ],
        [, , , , ],
        [1300000, 20000, 120000, 2000, 131222000],
        [1400000, 20000, 90000, 2000, 14102000]];

### one of your APIs
@app.route("/api/weeklydata")
def the_Weekly_Data_Method():
    return jsonify(someWeeklyPerformanceData)

@app.route("/api/salarydata")
def the_Method_for_some_Salary_Data():
    return jsonify(theDataForSalaries)

@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
