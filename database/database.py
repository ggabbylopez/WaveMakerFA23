from pymongo import MongoClient
import datetime

# Authors / Changes Made: TEAM D, COMP523 Fall 23

# this method needs to be called from the record_pistons function in Model.py
def update_database(current_date, interval_label, time_label, data):
    # connected to localhost
    client = MongoClient("mongodb://127.0.0.1:27017/")

    # database is called wavemaker_db, collection is called general_collection
    # these will be the only database and collection created and will store all data
    db = client.wavemaker_db
    collection = db.general_collection

    # _id field is generated by MongoDB
    collection.insert_one({"Date": current_date, "Interval": interval_label, "Time": time_label, "Data": data})



def query_database(query):
    # Format of query should be the following
    # query = {"date": "%m%D%Y %H:%M:%S"}

    # Connecting to database
    client = MongoClient("mongodb://127.0.0.1:27017/")
    db = client.wavemaker_db
    collection = db.general_collection

    return collection.find(query)


runs = query_database({})

for run in runs:
    print(run)