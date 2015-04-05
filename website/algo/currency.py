#!/usr/local/bin/python
import match

def priceSaved(user, schedule):
    start = None 
    end = None 
    tmp = user
    while tmp.prevUser is not None:
        tmp = tmp.prevUser
    
    start = tmp 
    tmp = user

    while tmp.nextUser is not None:
        tmp = tmp.nextUser

    end = tmp 
    tmp = start
    totalPrice = 0;

    while tmp is not None:
        totalPrice += tmp.regular 
        tmp = tmp.nextUser

    obj = schedule.find_one({'src':start.source,'dest':end.destination})
    price = obj.price
    #finish above after database is setup

    
    percentSaved = price/float(totalPrice)
    tmp = start

    while tmp is not None:
        tmp.savings = tmp.regular - (tmp.regular * percentSaved)
        tmp = tmp.nextUser

    






        
