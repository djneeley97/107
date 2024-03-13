import pymongo
import certifi

con_str = "mongodb+srv://FSDI:Test123@107.7chbdfm.mongodb.net/?retryWrites=true&w=majority&appName=107"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("organika")