import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client['test']
student = {
    'name':'pyt',
    'age':200,
    '_id':2,
}
collenction = db['test']
result = collenction.insert_one(student)
print(result)