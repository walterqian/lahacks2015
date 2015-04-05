#!/usr/local/bin/python
from flask import Flask
from pymongo import Connection
import pymongo

class User(object):

    def __init__(self, src, dest, depart, lines):
        self.source = src
        self.destination = dest
        self.departTime = depart
        self.railLines = lines
        self.matched = False
        self.savings = 0
        self.regular = 0
        self.nextUser = None
        self.prevUser = None

class Places(object):

    def __init__(self, name, times):
        self.station = name
        self.times = times

<<<<<<< HEAD
# Going to be hardcoded for now
locations = ['SD', 'LA', 'SB', 'SF']

Amy = User('SD', 'LA', '10:00 am', 'Pacific')
Bob = User('LA', 'SF', '12:00 pm', 'Pacific')
C = User ('LA', 1,1 ,1 )
D = User(1,'SD',1,1)

users = []

def addUser(userList, user):
    print "was here"
    for potential in userList:
        #TODO: time & rails
=======
def addUser(schedule, userList, user):
    for potential in userList.find():
>>>>>>> 6379774f48773f440c0dba537f2dee1a34e585f8
        if (potential.source == user.destination and potential.prevUser is None): 
            potential.prevUser = user
            user.nextUser = potential
            print "Connecting %s and %s" % (potential.source, user.destination)
            break
        elif (potential.destination == user.source and potential.nextUser is None):
            potential.nextUser = user
            user.prevUser = potential
            print "Connecting %s and %s" % (potential.destination, user.source)
            break
    userList.append(user)
<<<<<<< HEAD

addUser(users, Amy)
addUser(users, Bob)
addUser(users, C)
addUser(users,D)
=======
>>>>>>> 6379774f48773f440c0dba537f2dee1a34e585f8
