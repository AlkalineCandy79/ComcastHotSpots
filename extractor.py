import urllib
import urllib2

#url = 'https://hotspots.wifi.comcast.com/ajax/map-search'
#values = {'txtSearch' : 'Walnut+Creek',
#          'typeFilter' : [],
#          'clat' : '37.894218',
#         'clon' : '-122.075242'}
#data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()

#print (the_page)


## Bounding Box

url = 'https://hotspots.wifi.comcast.com/ajax/map-search'
values = {'txtSearch' : 'Bellevue',
          'typeFilter' : [],
          'tllat' : '47.666623',
          'tllon' : '-122.236483',
          'brlat' : '47.531808',
          'brlon' : '-22.084008'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print (the_page)

# build out the rest of the code.
