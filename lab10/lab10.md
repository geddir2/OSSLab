## 1
![alt text](checkpoint1.png)

## 2
![alt text](checkpoint2.png)

## 3
.find() returns a list of 20 definitions, and you have the option to view more
.findOne() Returns one document that satisfies the specified query criteria on the collection or view.
.find({word: "Capitaland"}) finds the word Capitaland and returns the definition of the word too
.find({_id: ObjectId("56fe9e22bad6b23cde07b8ce")}) returns the word price chopper and the definition in the dictonary

![alt text](checkpoint3-1.png)
![alt text](checkpoint3-2.png)
![alt text](checkpoint3-3.png)


## 4 

code:
```python
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

client = MongoClient()

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    db = client["mongo_db_lab"]
    collection = db["definitions"]

    all = list(collection.find())
    pp.pprint( all )

    one = collection.find_one()
    pp.pprint( one )

    specific = collection.find_one({"word": "Beer"})
    pp.pprint( specific )

    byId = collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ca")})
    pp.pprint( byId )

    insert = {"word": "Huge", "definition": "HUUUUGGGEEEEE"}
    collection.insert_one(insert)
    insertedWord  = collection.find_one({"word": "Huge"})
    pp.pprint( insertedWord )

```
output: 
![alt text](checkpoint4.png)
