#!/usr/local/bin
from random import randint
import linecache


cities=['SAC','LAX','DAV','SAC','BKY','OAC','SAN','SFP','LAX','SJC','SFP','OAC','SAC','SCC','SLO','LAX','SBA','GVB','BUL','SJC','SFP','SAN','SBA','VEC','GDL','LAX','FUL','ANA','IRV','OAC','SOL','OLT','SAN']
NUM=len(cities)
out = open('users', "w")
i=0
while (i<10000):

	src=cities[randint(0,NUM-1)]
	dest=cities[randint(0,NUM-1)]
	while (src==dest):
		dest=cities[randint(0,NUM-1)]
	line=src+','+dest

        time=linecache.getline('final', randint(1, 1382))
        value = time.split(',')


	line=line+','+value[3] +','+ value[4]
        out.write(line)
	i+=1

out.close()
