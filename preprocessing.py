
import numpy as np
import rasterio
import logging
import os
import pandas as pd
from rasterio.windows import Window
from matplotlib import pyplot
import matplotlib.pyplot as plt
import geopandas as gdp
import geopandas as gpd
from shapely.geometry import Point
from shapely.geometry import box
import requests #http framework to make mhvpl requests for routes
import json # handle response as json
from geopy.distance import vincenty
import pickle

log = logging.getLogger(__name__)

def split(map_file,origin,plot=False):
    """
    Split a window row in 4 parts, and return new rows results
    """
    origins=pd.DataFrame()
    window=int(origin.window/2)
    for left_x in np.arange(origin.left_x,origin.right_x,window):
        for top_y in np.arange(origin.top_y,origin.bottom_y,window):
            out=get_pop(map_file,left_x,top_y,window,plot=plot)
            if out != {}:
                origins=origins.append([out])
    return origins

def n_closest_geodetic(destinations,origins,n_keep,verbose=False):
    """
    Given a list of origins and destinations, return the "keep" number
    of destinations that are closest geodetically to each origin.

    Input: destinations,origins <Geopandas>
    Output: destinations filtered <Geopandas>
    """
    destinations=destinations.to_crs(origins.crs)
    filtered=gdp.GeoDataFrame()

    if verbose:
        i=0
        l=len(origins.index)
    for index in origins.index:
        if verbose:
            i=i+1
            print("Doing %i of %i\r"%(i,l),end="")
        distances=destinations.distance(origins.loc[index].geometry)
        if len(distances) < n_keep:
            n_keep = len(distances)
        #query indices
        indices=np.argsort(distances.values)[:n_keep]
        values=np.sort(distances.values)[:n_keep]
        #destination indices
        d_indices=distances.index[indices]
        filtered = filtered.append(destinations.iloc[indices])

    if verbose:
        print('done')
    return filtered.append(filtered).drop_duplicates(inplace=False)
