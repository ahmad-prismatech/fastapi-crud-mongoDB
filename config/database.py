from pymongo import MongoClient

MONGO_CONNECTION_STRING = "mongodb://localhost:27017"

client = MongoClient(MONGO_CONNECTION_STRING)

db = client.todo_application

collection_name = db["todos_app"]