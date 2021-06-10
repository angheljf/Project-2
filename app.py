from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/Market_db")

@app.route("/")
def home():
    
    data = mongo.db.jobs.find()
    

    return render_template('index.html', data=data)



if __name__ == "__main__":
    app.run(debug=True)

