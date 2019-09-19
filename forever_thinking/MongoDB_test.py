import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client['test']
student = {
    '_id':2,
    'name':'pyt',
    'age':200,
}
collenction = db['test']
result = collenction.insert_one(student)
print(result)