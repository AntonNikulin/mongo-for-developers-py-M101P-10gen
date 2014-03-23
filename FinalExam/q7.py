from pymongo import MongoClient

client = MongoClient()
db = client.test

images = db.images
albums = db.albums

for image in images.find():
	counter = db.albums.find({"images":image["_id"]}).count()
	if counter == 0:
		images.remove(image)