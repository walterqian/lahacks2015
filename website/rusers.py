from random import randint
import random



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

	minute='00'
	ampm='am'
	if (random.random()<0.5):
		minute='30'
	if (random.random()<0.5):
		ampm='pm'

	time=str(randint(1,12))+':'+minute+ampm

	line=line+','+time
	out.write(line+'\n')
	i+=1

out.close()