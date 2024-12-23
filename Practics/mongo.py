# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")      #connection with mongodb server

# db = client["College"]     #database

# collection = db["Student"]      #collection

# ack = collection.insert_many([{"name":"Sanket","age":"21","Marks":0},
#                              {"name":"Sandesh","age":"21","Marks":0},
#                              {"name":"Sanjana","age":"21","Marks":0}
#                              ])


# # collection.delete_one({'name':'Suvarna'})
# # collection.delete_many({"age":"21"})


# #update
# # collection.update_one({'name':'Sanket'},{"$set":{'Marks':500}})

# #update many
# # collection.update_many({'Marks':0},{'$inc':{'Marks':100}})      #lt gt dec
# # collection.update_many({"Marks":{'$lt':500}},{'$set':{'Marks':200}})

# # collection.delete_many({'name': {'$regex':"^S"}})           #delete data whenre name starts from S

# for i in collection.find():
#     print(i)





#session
# session = client.start_session()      #return session object
# #client._end_sessions

# session.start_transaction()
# session.abort_transaction()
# session.commit_transaction()


from pymongo import MongoClient,errors 

client = MongoClient("mongodb://localhost:27017/")      #connection with mongodb server

db = client["College"]     #database

collection = db["Student"]      #collection

# try:
#     session = client.start_session()
#     session.start_transaction()
#     collection.insert_one({'_id':100,'name':'sam','age':21})
#     collection.insert_one({'_id':200,'name':'suvarna','age':22})
# except errors.DuplicateKeyError as e:
#     print(e)
#     session.abort_transaction()
#     session.end_session()
# else:
#     session.commit_transaction()
#     print("Data entered successfully")
# finally:
#     session.end_session()

# cursor = collection.insert_many([{'name':'sam','age':21},
#                         {'name':'suv','age':22},{'name':'sam','age':21},
#                         {'name':'suv','age':22},{'name':'sam','age':21},
#                         {'name':'suv','age':22}])

# print (cursor)

