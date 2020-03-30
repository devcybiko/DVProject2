from flask import Flask, jsonify, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
import json

### create a flask instance
app = Flask(__name__)

### database Parameters
HOSTNAME="127.0.0.1"
PORT="5432"
USER="postgres"
PASSWORD="password"
DATABASE="project2"
SCHEMA = "public"

def DatabaseConnection():
    ### Database connection
    global Matches, Players, engine
    rds_connection_string = f"{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    print(rds_connection_string)
    engine = create_engine(f'postgresql://{rds_connection_string}')

    ### Map the engine to the Database
    Base = automap_base(bind=engine)
    Base.prepare(engine, reflect=True)
    keys = Base.classes.keys()
    print(Base.classes.keys())

    ### Get the database tables
    Matches = Base.classes.matches
    Players = Base.classes.players
    print("Connected")

### Hard-coded data
### Not for production/project delivery
### Just for examples
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
        {'Salaries':1300000, 'Office':20000, 'Merchandise':70000, 'Legal':2000, 'Total':130902000},
        {'Salaries':1300000, 'Office':20000, 'Merchandise':120000, 'Legal':2000, 'Total':131222000},
        {'Salaries':1400000, 'Office':20000, 'Merchandise':90000, 'Legal':2000, 'Total':14102000},
]

### one of your APIs
@app.route("/api/weeklydata")
def the_Weekly_Data_Method():
    return jsonify(someWeeklyPerformanceData)

### another potential API
@app.route("/api/salarydata")
def the_Method_for_some_Salary_Data():
    return jsonify(theDataForSalaries)

### an api to get all the Matches from the database
@app.route("/api/matches")
def get_me_some_matches():
    global Matches, engine
    results = []
    session = Session(engine)
    query = session.query(Matches)
    rows = query.statement.execute().fetchall()
    for row in rows:
        match = dict(row)
        results.append(match)
    return jsonify(results)

@app.route("/api/age_matches")
def get_me_some_age_based_matches(minage, maxage):
    global Matches, engine
    results = []
    session = Session(engine)
    query = session.query(Matches)
    rows = engine.execute(f"select * from matches where {minage} <= winner_age and winner_age <= {maxage}")
    for row in rows:
        match = dict(row)
        results.append(match)
    return jsonify(results)

@app.route("/api/players")
def get_me_some_players_please():
    global Players, engine
    results = []
    rows = engine.execute("select country_code, hand, count(first_name) as cnt from players group by country_code, hand having hand in ('L', 'R') order by hand, cnt desc, country_code")
    for row in rows:
        match = dict(row)
        results.append(match)
    return jsonify(results)

### the 'home' route. 
### NOTE: This allows sending data to the HTML through templating
## But you'll likely not need it since most of what you're doing is AJAX APIs
@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/results")
def results(minage, maxage):
    return render_template('results.html', minage=minage, maxage=maxage)

@app.route("/<page>")
def any_page(page):
    return render_template(page)


### A required way of saying "Start the server"
if __name__ == "__main__":
    DatabaseConnection()
    app.run(debug=True)
