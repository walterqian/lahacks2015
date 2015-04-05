#!/usr/local/bin/python

import currency
import match
import mongoDB

from flask import Flask
from pymongo import Connection
import pymongo

def main():
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

        userList = db.users
        schedule = db.schedules
        


if __name__ == '__main__':
    main()

