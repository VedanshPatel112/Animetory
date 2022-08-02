from re import T
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient("mongodb+srv://Vedansh:OzBXLeDpbvgm1tSv@cluster0.l6z8n.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client['zyx']
mydata = db['test']

mydict = { "name": "John", "address": "Highway 37" }

x = mydata.insert_one(mydict)

name = input("enter your name ")
age = int(input("enter your age "))
d = {
    "name":name,
    "age":age
}
x = mydata.insert_one(d)
