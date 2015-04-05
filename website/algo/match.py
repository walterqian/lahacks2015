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

    def changeSavings(saved):
        self.savings = saved

class Places(object):

    def __init__(self, name, times):
        self.station = name
        self.times = times

