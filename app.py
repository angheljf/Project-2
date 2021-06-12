from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

app = Flask(__name__)
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'Market_db'
COLLECTION_NAME = 'jobs'
FIELDS = {'Job Title':True, 'Min Salary Estimate':True, 'Max Salary Estimate':True, 'Avg Salary Estimate':True, 'Rating':True, 
'Location':True, 'Size':True, 'Type of ownership':True, 'Sector':True, 'Latitude': True, 'Longitude': True, 'Industry':True, '_id': False}

mongo = PyMongo(app, uri="mongodb://localhost:27017/Market_db")

@app.route("/")
def home():
    
    data = mongo.db.jobs.find()
    

    return render_template('index.html', data=data)

@app.route("/api")
def heat():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

@app.route("/cluster")
def clut():

    return render_template('cluster.html')

@app.route("/graph")
def graph():

    return render_template('graph.html')

@app.route("/graph2")
def graph2():

    return render_template('graph2.html')

if __name__ == "__main__":
    app.run(debug=True)

