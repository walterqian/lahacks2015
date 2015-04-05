#!/usr/local/bin/python
from flask import Flask
from pymongo import Connection
import pymongo

class User(object):

    def __init__(self, src, dest, depart, arrive, lines):
        self.source = src
        self.destination = dest
        self.departTime = depart
        self.arrivalTime = arrive
        self.railLines = lines
        self.matched = False
        self.savings = 0
        self.regular = 0
        self.nextUser = None
        self.prevUser = None

class Places(object):
e
    def __init__(self, name, times):
        self.station = name
        self.times = times

# Going to be hardcoded for now


def addUser(userList, user):
    # schedule for times
    # userList is database of our users

    for potential in userList.find():

        if (potential.source == user.destination and potential.prevUser is None and user.arrivalTime == potential.departTime): 
            potential.prevUser = user
            user.nextUser = potential
            potential.matched = True 
            user.matched = True
            print "Connecting %s and %s" % (potential.source, user.destination)
            break
        elif (potential.destination == user.source and potential.nextUser is None and potential.arrivalTime == user.departTime):
            potential.nextUser = user
            user.prevUser = potential
            potential.matched = True
            user.matched = True
            print "Connecting %s and %s" % (potential.destination, user.source)
            break
    userList.append(user)

