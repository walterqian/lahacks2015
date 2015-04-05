#!/usr/local/bin/python
import match

def priceSaved(user):
    start = None 
    end = None 
    tmp = user
    while (tmp.prev != None):
        tmp = tmp.prev
    
    start = tmp 
    tmp = end 

    while (tmp.next != None):
        tmp = tmp.next

    end = tmp 
    tmp = start
    totalPrice = 0;
    
    while (tmp.next != None):
        totalPrice += tmp.regular 

    price = getPriceFromServer(start,end)
    #finish above after database is setup

    percentSaved = price/totalPrice
    tmp = start
    while (tmp.next != None):
        tmp.savings = (tmp.regular * percentSaved)






        
