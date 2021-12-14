from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape
from mars_scrape import scrape
import pymongo
from flask import Flask, jsonify

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsdata_db"
mongo = PyMongo(app)
#conn = 'mongodb://localhost:27017/marsdata_db'
#client = pymongo.MongoClient(conn)

#db = client.marsdata_db
#mdata=db.data
mdb = mongo.db

@app.route('/')
def index():
    mars = mongo.db.data.find_one()
    #mars_data=list(mdata.find())
    return render_template('index.html', data=mars)

@app.route('/scrape')
def scraper():
    mdata=mdb.data
    marsdata=mars_scrape.scrape()
    mdata.update_one({}, {"$set": marsdata}, upsert=True)
    return redirect('/',code=302)

if __name__ == "__main__":
    app.run(debug=True)
