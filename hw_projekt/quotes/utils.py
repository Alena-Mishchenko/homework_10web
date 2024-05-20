from pymongo import MongoClient
import os
from pymongo.server_api import ServerApi
# from mongoengine import connect

# current_directory = os.path.dirname(os.path.abspath(__file__))
# connect(
#     db="homework8",
#     host="mongodb+srv://goitlearn:mypas@cluster0.nlahlds.mongodb.net/?retryWrites=true&w=majority",
# )



def get_mongodb():
    client = MongoClient("mongodb+srv://goitlearn:mypas@cluster0.nlahlds.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
    db = client.homework_10
    return db
