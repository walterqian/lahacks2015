#!/usr/local/bin/python
import match

def priceSaved(user):
    start = None 
    end = None 
    tmp = user
    while (tmp.prevUser != None):
        tmp = tmp.prevUser
    
    start = tmp 
    tmp = end 

    while (tmp.nextUser != None):
        tmp = tmp.nextUser

    end = tmp 
    tmp = start
    totalPrice = 0;
    
    while (tmp.nextUser != None):
        totalPrice += tmp.regular 

    price = getPriceFromServer(start.source,end.destination)
    #finish above after database is setup

    percentSaved = price/totalPrice
    tmp = start
    while (tmp.next != None):
        tmp.savings = (tmp.regular * percentSaved)
        tmp = tmp.nextUser






        
