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
