#!/usr/bin/env python
######################
# This program returns Eastings and Northings of user defined longitude and latitude.
# I used the pyproj package (https://code.google.com/p/pyproj/) which acts as an interface
# between python and  the proj.4 projection library (http://trac.osgeo.org/proj/).
# Mostly, I copied code from this blog post: http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/



import pyproj

long = -1.63
lat = 53.29
 
## Define projections using EPSG codes
osgb36=pyproj.Proj("+init=EPSG:27700") # UK Ordnance Survey, 1936 datum
wgs84=pyproj.Proj("+init=EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth


x,y =pyproj.transform(wgs84,osgb36,long,lat)
# transforms from wgs84 to osgb36 i.e. returns long and lat as eastings and northings.

print x, y
    
    