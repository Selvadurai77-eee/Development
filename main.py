import pyproj
import pandas as pd
import geopandas as gpd
import geopy

geopy.geocoders.options.default_user_agent = "my-application"

def geocode(locations):
    df = pd.read_csv(r"E:\Selvadurai\Programming\Python\Projects\Dev\test.csv")
    return [gpd.tools.geocode(locations[i],provider = 'bing', api_key="AjE7UwKcn26Slp-CTvz3MKFf9OUYn_BALfPcxp_kRKSdJhiOqxoy_b_RF2zDRTKk") for i in range(len(locations))]


def find_distance(x1,y1,x2,y2):
    lat1,long1 = y1,x1
    lat2,long2 = y2,x2
    geod = pyproj.Geod(ellps="WGS84")
    angle1,angle2,distance = geod.inv(long1, lat1, long2, lat2)
    return distance /1000




if __name__ == "__main__":
    df = pd.read_csv(r"E:\Selvadurai\Programming\Python\Projects\Dev\test.csv")
    points = geocode([df['Place1'],df['Place2']])
    x1 , y1  = points[0]['geometry'][0].x , points[0]['geometry'][0].y
    x2 , y2  = points[1]['geometry'][0].x , points[1]['geometry'][0].y
    print(find_distance(x1, y2 , x2, y2))
    geocode([df['Place1'],df['Place2']])
    