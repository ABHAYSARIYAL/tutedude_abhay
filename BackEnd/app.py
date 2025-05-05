from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

URI = os.getenv('URI')


# # Create a new client and connect to the server
client = MongoClient(URI)
# db = client.text
# collection = db['Flask']


# Create a new client and connect to the server
#client = MongoClient(URI, server_api=ServerApi('1'))
db = client.text
collection = db['Flask']


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



#creating home page
app = Flask(__name__)



#creating the submit 
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return 'data submitted succesfully'

@app.route('/View')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']

    data = {
        'data' : data
    }
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug = True)
