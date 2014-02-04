import bottle
import pymongo

@bottle.route("/")
def index():
	connection = pymongo.MongoClient("localhost", 27017)
	
	#attach to test database
	db = connection.test

	#get handle for names collection
	name = db.names

	item = name.find_one()

	return "<b>Hello %s!" % item["name"]

bottle.run(host="localhost", port=8000)