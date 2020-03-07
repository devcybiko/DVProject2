from flask import Flask, jsonify, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.automap import automap_base

### create a flask instance
app = Flask(__name__)

### database Parameters
HOSTNAME="PostgreSQL 12"
PORT="5432"
USER="postgres"
PASSWORD="hoxan9"
DATABASE="project2"
SCHEMA = "public"

def DatabaseConnection():
    ### Database connection
    rds_connection_string = f"{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    print(rds_connection_string)
    engine = create_engine(f'postgresql://{rds_connection_string}')
    print("engine created")

    ### Map the engine to the Database
    metaData = MetaData(schema=f"{SCHEMA}")
    Base = automap_base(bind=engine, metadata=metaData)
    keys = Base.classes.keys()
    print("got base")
    print(keys)
    print("automapped")
    Base.prepare(engine, reflect=True)
    print("prepared")

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
    matches = Matches.query.all()
    return jsonify(matches)

@app.route("/api/players")
def get_me_some_players_please():
    players = Players.query.all()
    return jsonify(players)

### the 'home' route. 
### NOTE: This allows sending data to the HTML through templating
## But you'll likely not need it since most of what you're doing is AJAX APIs
@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


### A required way of saying "Start the server"
if __name__ == "__main__":
    DatabaseConnection()
    app.run(debug=True)
