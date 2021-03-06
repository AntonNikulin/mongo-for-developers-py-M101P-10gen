#M101P: MongoDB for Developers  
###Building blog with mongoDB and Bottle framework
---
Working files, snippets and homeworks.  

__requirements:__ 

*   mongodb 2.2.7 
*   python 2.7
*   Bottle 0.11
*   pymongo 2.6.3

__content:__

*	2-2 Write a program in the language of your choice that will remove the grade of type "homework" with the lowest score for each student from the dataset that you imported in HW 2.1. Since each document is one grade, it should remove one document per student.
*   4-3 Use indexes.Your assignment is to make the following blog pages fast:
######FinalExam:
*	q1 Construct a query to calculate the number of messages sent by Andrew Fastow, CFO, to Jeff Skilling, the president. Andrew Fastow's email addess was andrew.fastow@enron.com. Jeff Skilling's email was jeff.skilling@enron.com. 
*	q2 Please use the Enron dataset you imported for the previous problem. For this question you will use the aggregation framework to figure out pairs of people that tend to communicate a lot. To do this, you will need to unwind the To list for each message. Which pair of people have the greatest number of messages in the dataset?
*	q7 You have been tasked to cleanup a photosharing database. The database consists of two collections, albums, and images. Every image is supposed to be in an album, but there are orphan images that appear in no album. Here are some example documents (not from the collections you will be downloading).
> db.albums.findOne()
{
	"_id" : 67
	"images" : [
		4745,
		7651,
		15247,
		17517,
		17853,
		20529,
		22640,
		27299,
		27997,
		32930,
		35591,
		48969,
		52901,
		57320,
		96342,
		99705
	]
}
> db.images.findOne()
{ "_id" : 99705, "height" : 480, "width" : 640, "tags" : [ "dogs", "kittens", "work" ] }
From the above, you can conclude that the image with _id = 99705 is in album 67. It is not an orphan.
Your task is to write a program to remove every image from the images collection that appears in no album. Or put another way, if an image does not appear in at least one album, it's an orphan and should be removed from the images collection.
When you are done removing the orphan images from the collection, there should be 89,737 documents in the images collection. To prove you did it correctly, what are the total number of images with the tag 'kittens" after the removal of orphans? As as a sanity check, there are 49,932 images that are tagged 'kittens' before you remove the images.