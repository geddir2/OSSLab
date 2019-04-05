from pymongo import MongoClient
import random
import datetime
import pprint


client = MongoClient()

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client["mongo_db_lab"]
    collection = db["definitions"]
    index = random.randint(1, collection.count() )
    word = list(collection.find())[index]
    
    collection.update_one({"word": word["word"]}, {"$push": {"dates": datetime.datetime.now()} } )
    
    
    return word


if __name__ == '__main__':
    print (random_word_requester())
