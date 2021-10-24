from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, port):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:%d/AAC' % (username, password, port))
        self.database = self.client['AAC']
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary       
            return result.acknowledged
        else:
            raise Exception('Nothing to save, because data parameter is empty')
        return False
            
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data, {"_id":False})
        else:
            raise Exception('Nothing to read, because data parameter is empty')
            
    def update(self, data, newdata):
        if data is not None and newdata is not None:
            result = self.database.animals.update_one(data, newdata)
            if result.acknowledged:
                return result.raw_result
        else:
            raise Exception('One or more data parameters are empty')
    
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.acknowledged:
                return result.raw_result
        else:
            raise Exception('Nothing to delete, because data parameter is empty')