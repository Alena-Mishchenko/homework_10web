import json
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
# client = MongoClient("mongodb://localhost")

client = MongoClient(
    "mongodb+srv://goitlearn:mypas@cluster0.nlahlds.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
current_directory = os.path.dirname(os.path.abspath(__file__))
authors_file_path = os.path.join(current_directory, 'authors.json')
quotes_file_path = os.path.join(current_directory, 'quotes.json')
db = client.homework_10

with open(quotes_file_path, 'r', encoding='UTF-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id']) 
        })
