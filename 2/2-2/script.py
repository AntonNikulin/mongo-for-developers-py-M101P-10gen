from pymongo import MongoClient

"""
document example:
{ "_id" : { "$oid" : "50906d7fa3c412bb040eb577" }, "student_id" : 0, "type" : "exam", "score" : 54.6535436362647 }
Write a program in the language of your choice that will remove the grade of type "homework"
with the lowest score for each student from the dataset that you imported in HW 2.1.
Since each document is one grade, it should remove one document per student.
"""
#connect on default host and port at localhost:27017
client = MongoClient()

db = client['students']
collection = db['grades']

currentStudent = 0
prevStudent = 0
minValue = None
for rec in collection.find({'type':'homework'}).sort([('student_id', 1),('score', 1)]):
    currentStudent = rec['student_id']
    #Find out if student_id changed
    if currentStudent != prevStudent:
        prevStudent = currentStudent
        print "Student changed to "+str(prevStudent)

    print rec['student_id']