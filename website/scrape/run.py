from bs4 import BeautifulSoup
import urllib   
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#get cities
cities=['SAC','DAV','BKY','OAC','SFP','SJC','SCC','SLO','GVB','BUL','SBA','VEC','GDL','LAX','FUL','ANA','IRV','SOL','OLT','SAN']
# with open('codes') as f:
#     content = f.readlines()
#     for line in content:
#     	tmp=line[-4:].strip()
#     	if (tmp is not ''):
# 	    	cities.append(tmp)

data=[]

driver = webdriver.Firefox()
driver.get("http://tickets.amtrak.com/itd/amtrak")
count=0
index=0

for u in range(0,len(cities)):
	for k in range(0,len(cities)):
		if (cities[u]==cities[k]):
			continue

		ele = driver.find_element_by_name("wdf_origin")
		ele.clear()
		ele.send_keys(cities[u])
		ele=driver.find_element_by_name("wdf_destination")
		ele.clear()
		ele.send_keys(cities[k])
		ele.send_keys(Keys.RETURN)
		soup=BeautifulSoup(driver.page_source)


		for form in soup.find_all(attrs={"name":re.compile("selectTrainForm")}):
			timeTags=form.find_all('div','ffam-time')
			t='-'
			if (len(timeTags)>1):
				t=timeTags[0].string.strip()+'|'+timeTags[len(timeTags)-1].string.strip()
			else:
				t=timeTags[0].string.strip()
			if (t is ''):
				t='-'

			priceSuperTag=form.find('td','ffam-third-col')
			p='-'
			if (priceSuperTag is not None):
				priceTag=priceSuperTag.find('span')
				if (priceTag is not None):
					p=priceTag.string.strip()

			d=()
			d=d+(cities[u],cities[k],p,t,)
			data.append(d)
			count+=1

		#output
		if (count>100):
			name='output-'+str(index)
			f = open(name, "w")
			for d in data:
				f.write(','.join(d)+'\n')
				print d
			f.close()
			index+=1
			count=0
			data=[]
			#wait for 20 sec
			print "Sleeping..."
			time.sleep(20)
			print "Start again"

print "Done!"
driver.close()
