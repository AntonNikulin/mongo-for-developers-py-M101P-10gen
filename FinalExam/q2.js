use enron
//Find greatest number of messages in the dataset
db.messages.aggregate([
{$project: {"headers.To":1, "headers.From":1}},
{$unwind: "$headers.To"},
{$group: {_id:{from:"$headers.From", to:"$headers.To"}, 
			total:{$sum:1}}},
{$sort:{total:-1}},
{$limit:5}
])

//Check the data:
//sum : count
//2181 : 116
db.messages.find({$and:[{'headers.From':'veronica.espinoza@enron.com'}, {'headers.To':'recipients@enron.com'}]}).count()

//974 : 616
db.messages.find({$and:[{'headers.From':'susan.mara@enron.com'}, {'headers.To':'richard.shapiro@enron.com'}]}).count()

//750 : 750 <-- greatest number without duplication
db.messages.find({$and:[{'headers.From':'susan.mara@enron.com'}, {'headers.To':'jeff.dasovich@enron.com'}]}).count()

//708 : 355
db.messages.find({$and:[{'headers.From':'susan.mara@enron.com'}, {'headers.To':'james.wright@enron.com'}]}).count()