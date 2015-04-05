#!/usr/local/bin/python

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

# Going to be hardcoded for now
locations = ['SD', 'LA', 'SB', 'SF']

Amy = User('SD', 'LA', '10:00 am', 'Pacific')
Bob = User('LA', 'SF', '12:00 pm', 'Pacific')

users = []

def addUser(userList, user):
    for potential in userList:
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

addUser(users, Amy)
addUser(users, Bob)
