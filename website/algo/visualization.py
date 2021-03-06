#!/usr/local/bin/python


from flask import Flask
from pymongo import Connection
import pymongo



def main():

    a = getStations()
    b = a.head
    while b is not None:
        print b.data
        b = b.next
        
        
        
        

class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoubleList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
 
            current_node = current_node.next
        print "*"*50
    
    
def getStations():
    stations = DoubleList()
       
    # from north to south
    # ['SAC','DAV','BKY','OAC','SFP','SJC','SCC','SLO','GVB','BUL','SBA','VEC','GDL','LAX','FUL','ANA','IRV','SOL','OLT','SAN']
    stations.append('SAC')
    stations.append('DAV')
    stations.append('BKY')
    stations.append('OAC')
    stations.append('SFP')
    stations.append('SJC')
    stations.append('SCC')
    stations.append('SLO')
    stations.append('GVB')
    stations.append('BUL')
    stations.append('SBA')
    stations.append('VEC')
    stations.append('GDL')
    stations.append('LAX')
    stations.append('FUL')
    stations.append('ANA')
    stations.append('IRV')
    stations.append('SOL')
    stations.append('OLT')
    stations.append('SAN')

    return stations 

if __name__ == '__main__':
    main()
