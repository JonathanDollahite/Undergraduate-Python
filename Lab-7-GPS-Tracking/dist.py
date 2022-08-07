import math
import numpy as np

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

TECUMSEH_LAT = 38.982439
TECUMSEH_LON = -76.484226

MISSION_BEACH__LAT = 32.77
MISSION_BEACH__LON = -117.25

distance = gps_dist(TECUMSEH_LAT, TECUMSEH_LON, MISSION_BEACH__LAT, MISSION_BEACH__LON)
print('Distance:', distance, 'miles')
