## I wrote this for a past project and use now just as a basic reference for creating py lists, keys, and tuples --
## -- UTM projection parameters

# Assign lookup to dictionary or container
utm_lookup = {-147:'UTM Zone 6', -150, 'UTM Zone 5, -141:'UTM Zone 7'}
utm_lookup

utm_lookup.values()
utm_lookup.keys()
utm_lookup[-147] ## lookup[key]

central_meridian = -141

## Use to determine UTM zone
if (central_meridian == -150):
	print "UTM Zone 5"
elif (central_meridian == -147):
	print "UTM Zone 6"
elif (central_meridian == -141):
	print "UTM Zone 7"
else:
	print "Unknown UTM zone: Verify central_meridian assignment"

## Use dictionary to determine UTM zone
print utm_lookup[central_meridian]
central_meridian = -156
utm_lookup.has_key(central_meridian)

if (utm_lookup.has_key(central_meridian)):
	print utm_lookup[central_meridian]
else:
	print central_meridian, " not a value in dictionary"

## Function that returns UTM zone from input of negative longitude
def utm_zone(longitude):
	zone = int((longitude +180.0) / 6.0 + 1.0)
	print "UTM Zone = ", zone
	return zone
