
from flask import Flask
from pymongo import Connection
import pymongo

app = Flask(__name__)

# connect to server
print '\nConnecting ...'
conn = Connection('ds041177.mongolab.com', 41177)
 
# Get the database
print '\nGetting database ...'
db = conn['amrekt']
 
# Have to authenticate to get access
print '\nAuthenticating ...'
db.authenticate('user', 'password')
 
# Test
# test = db.test
# test.remove()
# test.insert({'id': 5,'score':6})
# test.insert({'id': 6, 'score':20})
# print '\nNumber of posts', test.find().count()
# print test.find_one({'id':5})

#load data
schedules = db.schedules
users = db.users

# schedules.remove()
# with open('scrape/final') as f:
# 	content = f.readlines()
# 	for line in content:
# 		val=line.split(',')
# 		schedules.insert({'src': val[0],'dest':val[1],'price':val[2],'depart':val[3],'arrival':val[4]})

allUsers = db.users

print '\nNumber of schedules', schedules.find().count()
print users.find().count()
print users.find({'src':'SAC'})
print allUsers.find_one()
