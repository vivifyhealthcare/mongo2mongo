from pymongo import MongoClient
import pymongo
import urllib.parse
try:
    y = []
    mongodb_dbname2 = "madhu"
    username = urllib.parse.quote_plus('devops_admin')
    password = urllib.parse.quote_plus('Devj0019ej')
    myclient2 = MongoClient('mongodb://%s:%s@3.108.11.120:27017' % (username, password))
    mydb2 = myclient2[mongodb_dbname2]
    migration = mydb2.list_collection_names()
    mongodb_host = "mongodb://localhost:e7017/"
    mongodb_dbname1 = "lifeeazydatabase"
    myclient1 = pymongo.MongoClient(mongodb_host)
    mydb1 = myclient1[mongodb_dbname1]
    print(myclient1)

    for col in migration:

        data = mydb2[col]

        for x in data.find():
            y.append(x)
        if y == []:
            mycol = mydb2[col]
            pass
        else:
            mycol = mydb1[col]
            mycol.insert_many(y)
            y.clear()
except pymongo.errors.BulkWriteError as e:
    print('Database is existing with is name')
except pymongo.errors.OperationFailure as e:
    print('Check the credentials of Mongodb')
except ValueError as e:
    print('Check the Local host of Mongodb')