from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:root@cluster0.wi5ns.gcp.mongodb.net/JWT?retryWrites=true&w=majority")
db = client.get_database('JWT')

