import os
import urllib.request
import math

#convert a lat/long to a tile reference
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

#new grey tiles
baseURL = 'http://maps-dev.tableausoftware.com/tile/d/mode=named%7Cfrom=tableau2_2_base/mode=named%7Cfrom=tableau2_2_roads/mode=named%7Copacity=.5%7Cfrom=tableau2_2_admin0_borders/mode=named%7Copacity=.5%7Cfrom=tableau2_2_admin0_labels/mode=named%7Copacity=.5%7Cfrom=tableau2_2_admin1_borders/mode=named%7Copacity=.5%7Cfrom=tableau2_2_admin1_labels/mode=named%7Cfrom=tableau2_2_place_labels/ol/'
URLsuffix ='.png?apikey=tabmapbeta'

#old, normal tiles
#baseURL = 'http://maps-dev.tableausoftware.com/tile/d/mode=named%7Cfrom=tableau1_2_base/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin0_borders/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin0_labels/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin1_borders/mode=named%7Copacity=.5%7Cfrom=tableau1_2_admin1_labels/ol/'
#URLsuffix ='.png?apikey=tabmapbeta'

root_dir='normal'

#bounding box to fetch
top_deg=-33
left_deg=150
bottom_deg=-35
right_deg=152

#range of zoom levels to calculate
min_level=12
max_level=14

if not os.path.isdir(root_dir):
  os.mkdir(root_dir)

#for each zoom level
for z in range(min_level, max_level + 1):
  if not os.path.isdir('%s\\%i' % (root_dir, z)):
    os.mkdir('%s\\%i' % (root_dir, z))

  topleft=deg2num(top_deg, left_deg, z)
  botright=deg2num(bottom_deg, right_deg, z)
  #there are 2^z tile stripes across
  for y in range(topleft[0],botright[0]):
    if not os.path.isdir('%s\\%i\\%i' % (root_dir, z, y)):
      os.mkdir('%s\\%i\\%i' % (root_dir, z, y))

    #there are 2^z tile stripes down
    for x in range(topleft[1],botright[1]):
      print("%i %i %i" % (z, y, x))

      #get the tile from the URL into a file
      URL='%s%i/%i/%i%s' % (baseURL, z,y,x, URLsuffix)
      fo='.\\%s\%i\\%i\\%i.png' % (root_dir, z, y, x)
      if not os.path.exists(fo):
        urllib.request.urlretrieve(URL, fo)
      

