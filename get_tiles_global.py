import os
import math
import urllib

#new grey tiles
baseURL = 'https://maps.tableausoftware.com/tile/d/mode=named%7Cfrom=tableau5_2_base/mode=named%7Cfrom=tableau5_2_water/mode=named%7Cfrom=tableau5_2_landcover/mode=named%7Cfrom=tableau5_2_water/mode=named%7Cfrom=tableau5_2_admin0_borders/mode=named%7Cfrom=tableau5_2_admin0_labels/mode=named%7Cfrom=tableau5_2_admin1_borders/mode=named%7Cfrom=tableau5_2_admin1_labels/ol/'
URLsuffix ='.png?apikey=tabmapbeta&size=304'

#old, normal tiles
#baseURL = 'http://maps.tableausoftware.com/tile/d/mode=named%7Cfrom=tableau1_2_base/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin0_borders/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin0_labels/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin1_borders/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin1_labels/ol/'
#URLsuffix ='.png?apikey=tabmapbeta'

#how deep will we zoom?
levels=8
if not os.path.isdir('normal'):
  os.mkdir('normal')

#for each zoom level
for z in range(0, levels + 1):
  if not os.path.isdir('normal\\%i' % (z)):
    os.mkdir('normal\\%i' % (z))
  
  #there are 2^z tile stripes across
  for y in range(0,(2**z)):
    if not os.path.isdir('normal\\%i\\%i' % (z,y)):
      os.mkdir('normal\\%i\\%i' % (z,y))

    #there are 2^z tile stripes down
    for x in range(0,(2**z)):
      print("%i %i %i" % (z, y, x))

      #get the tile from the URL into a file
      URL='%s%i/%i/%i%s' % (baseURL, z,y,x, URLsuffix)
      fo='.\\normal\%i\\%i\\%i.png' % (z, y, x)
      if not os.path.exists(fo):
        print str(URL + " -> " + fo)
        urllib.urlretrieve(URL, fo)
      

