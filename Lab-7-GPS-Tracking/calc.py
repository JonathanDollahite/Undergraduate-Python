import math
import numpy as np
from dateutil import parser

def hav(theta):
    """ Fill in the definition of hav() """
    #convert from degrees to radians
    theta = math.radians(theta)
    #This equation will return hav as the haversine of an angle in radians
    cos_theta = math.cos(theta)
    hav = (1 - cos_theta)/2
    return hav

def gps_dist(lat1, lon1, lat2, lon2):
    """ Fill in with calls to the hav() function and using the formula above """
    EARTH_RADIUS = 3958.7613
    #convert each of the arguments from degrees to radians
    lat1r = math.radians(lat1)
    lon1r = math.radians(lon1)
    lat2r = math.radians(lat2)
    lon2r = math.radians(lon2)

    #find difference between lats and lons, using degrees since hav already converts to radians
    dif_lats = lat2 - lat1
    dif_lons = lon2 - lon1

    #use hav function to find the haversine of the difference of lats and lons
    hav_lats = hav(dif_lats)
    hav_lons = hav(dif_lons)

    #find the cosine of lat1 and lat2 in radian form
    cos_lat1r = math.cos(lat1r)
    cos_lat2r = math.cos(lat2r)

    #do the rest of the equation and return d as the distance.
    sum = hav_lats + (cos_lat1r * cos_lat2r * hav_lons)
    root = math.sqrt(sum)

    arcsin = np.arcsin(root)
    d = 2 * EARTH_RADIUS * arcsin
    return d

##-----------------------------------------------------------------------------
##-----------------------------------------------------------------------------

x = input('Please enter a gps file: ')
#open the file and creat new lat and lon list
f = open(x, "r")
list = f.readlines()
lat = []
lon = []
n = 0
for string in list:
    new_list = string.split()
    lat.append(float(new_list[0]))
    lon.append(float(new_list[1]))
    n = n + 1

#calculate total distance
x = 0
total_distance = 0
while x < (n - 1):
    point2point = gps_dist(lat[x], lon[x], lat[x+1], lon[x+1])
    total_distance = total_distance + point2point
    x = x + 1

#calculate time interval
date_time1 = []
date_time2 = []

throw_away = list[0]
throw_away = throw_away.split()
date_time1 = throw_away[2] + ' ' + throw_away[3]

trash = list[n-1]
trash = trash.split()
date_time2 = trash[2] + ' ' + trash[3]

t1 = parser.parse(date_time1)
t2 = parser.parse(date_time2)
diff = t2 - t1
hours = diff.total_seconds() / 3600
avg_rate = diff / total_distance
avg_speed = total_distance / hours


#Print out result
print('Total distance:', total_distance, 'miles')
print('Total time:', diff)
print('Average rate:', avg_rate)
print('Average speed', avg_speed)
