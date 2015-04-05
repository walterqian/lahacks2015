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

