#!/usr/local/bin/python

class User(object):

    def __init__(self, src, dest, time, lines):
        self.source = src
        self.destination = dest
        self.time = time
        self.railLines = lines
        self.matched = False
        self.savings = 0
        self.regular = 0

class Places(object):

    def __init__(self, name, time):
        self.station = name
        self.time = time
