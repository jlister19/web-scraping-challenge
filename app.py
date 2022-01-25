from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

conn = 'mongodb://localhost:27017/'

client = pymongo.MongoClient(conn) 

# This is like saying "Use classDB" so db is now mars_db
db = client.mars_db

# drop records from the mars_tbl collection
db.mars_tbl.drop()

# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_app")

app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    planet_data = mongo.db.mars_tbl.find_one()

    # Return template and data
    return render_template("index.html", solarsystem=planet_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_tbl = mongo.db.mars_tbl
    print(mars_tbl)
    mars_dict = scrape_mars.scrape_fn()
    print(mars_dict)
    
    # Update the Mongo database using update and upsert=True
    # or use mars.update({}, mars_data, upsert=True)
    mars_tbl.update_one({},{"$set":mars_dict}, upsert=True)
    # mongo.db.collection.update({}, mars_data, upsert=True)
        
    # Redirect back to home page
    # or use mars.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)