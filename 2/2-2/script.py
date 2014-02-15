from pymongo import MongoClient

#connect on default host and port
client = MongoClient()

db = client['students']
collection = db['grades']

print collection.find_one()