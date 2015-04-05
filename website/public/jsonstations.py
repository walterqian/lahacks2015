import yaml

f = open('stationsabbr.json','r')


abbr = f.readline()
abbr = yaml.load(abbr)

f.close()

abbrev = {}
for key in abbr:
	lat = float(key.split(',')[0])
	abbrev[lat] = abbr[key]

print abbrev

tracks = []

f = open('amtraklines','r')
coordinates = f.readline().rstrip()
while coordinates:
	name = coordinates
	description = f.readline().rstrip()
	coordinates = f.readline().rstrip()
	stations = []
	while coordinates and not coordinates[0].isalpha():
		lat = float(coordinates.split(',')[0])
		if lat in abbrev:
			abbreviation = abbrev[lat]
		else:
			abbreviation = coordinates
		stations.append(abbreviation)
		coordinates = f.readline().rstrip()
	track = []
	track.append(name)
	track.append(description)
	track.append(stations)
	print track