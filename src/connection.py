# src/connection.py
from pymongo import MongoClient

client = MongoClient("mongodb://marcus:marcus@192.168.3.16:27017/")
db = client.teste_twitter
trends_collection = db.trends
