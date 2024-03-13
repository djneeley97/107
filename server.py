from flask import Flask, request
import json
from config import db

app = Flask(__name__)# __name__ this is using the name of the folder

@app.get("/")
def home ():
    return "hello from flask"
# hello

@app.get("/testing")
def test():
    return "hello from another page"

#create 2 more api (about and blog page)

@app.get("/about")
def about():
    me = {"name": "daniel"}
    return json.dumps(me)

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2", "build": 123456}
    return json.dumps(version)

@app.get("/blog")
def blog():
    return "this is the about page"

# read and write in to the server
@app.get("/api/products")
def get_products():
    
    return json.dumps(products)

products  = []
def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products")
def save_products():
    #should save a new product
    product = request.get_json()
    #print (product)   
    #mock the save

    # products.append(product)
    db.products.insert_one(product)

    return json.dumps(fix_id(product))


app.run(debug=True)# apply the changes on the code live


# api / endpoints 
# transform JSON / convert JSON in an object again