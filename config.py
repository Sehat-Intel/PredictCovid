from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.wi5ns.gcp.mongodb.net/predictCovid?retryWrites=true&w=majority")
db = client.get_database('predictCovid')

