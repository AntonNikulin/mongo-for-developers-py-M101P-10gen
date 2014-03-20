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

    The blog home page
    The page that displays blog posts by tag (http://localhost:8082/tag/whatever)
    The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)