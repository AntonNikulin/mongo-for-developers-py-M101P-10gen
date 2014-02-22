"""
Write a program in the language of your choice that will remove the lowest homework score for each student.
 Since there is a single document for each student containing an array of scores,
 you will need to update the scores array and remove the homework.
 { "_id" : 0, "name" : "aimee Zank", "scores" :
                                     [  { "type" : "exam", "score" : 1.463179736705023 },
                                        { "type" : "quiz", "score" : 11.78273309957772 },
                                        { "type" : "homework", "score" : 6.676176060654615 },
                                        { "type" : "homework", "score" : 35.8740349954354 }
                                     ] }
"""

from pymongo import MongoClient

client = MongoClient()
db = client.school
collection = db.students

for doc in collection.find():
    #get array of scores from document and sort it by type then score
    arr= sorted(doc['scores'], key=lambda x: (x["type"], x["score"]))
    #homework with lowest grade in 2nd place. delete it.
    del arr[1]
    print arr
