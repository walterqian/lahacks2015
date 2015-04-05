import re

regexp = re.compile("\(.+\)")

out = open('final', "w")
with open('output') as f:
    content = f.readlines()
    for line in content:
    	if regexp.search(line) is not None:
    		continue

    	line=line.replace('$','')
    	out.write(line)

f.close()
out.close()
