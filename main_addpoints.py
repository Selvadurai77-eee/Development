import pandas as pd
from osgeo import ogr
from osgeo import osr
import os

if __name__ == "__main__" :
    os.chdir(r"E:\Selvadurai\Programming\Python\Projects\Dev\Geo-Development")
    tids_df = pd.read_excel(os.path.join(os.getcwd(),"Input","ITS","TIDS_Locations.xlsx"), engine="openpyxl",index_col="No.")
    
    # Driver for ESRI Shapefile
    driver = ogr.GetDriverByName("ESRI Shapefile")

    # Shape file as Data Source
    dataSource = driver.CreateDataSource(os.path.join(os.getcwd(),"Output","TIDS_Locations.shp"))

    # Spatial Reference 
    spatialReference = osr.SpatialReference()
    spatialReference.SetWellKnownGeogCS("WGS84")

    # Layer TIDS in Shape file 
    layer = dataSource.CreateLayer("TIDS",spatialReference)
    
    # Field TIDS_ID
    fieldSchema = ogr.FieldDefn("TIDS_ID", ogr.OFTInteger)
    fieldSchema.SetWidth(3)
    layer.CreateField(fieldSchema)
    
    # Field Location Description 
    fieldSchema = ogr.FieldDefn("Location", ogr.OFTString)
    fieldSchema.SetWidth(250)
    layer.CreateField(fieldSchema)

    # Field Latitude
    fieldSchema = ogr.FieldDefn("Latitude", ogr.OFTString)
    fieldSchema.SetWidth(25)
    layer.CreateField(fieldSchema)

    # Field Laongitude
    fieldSchema = ogr.FieldDefn("Longitude", ogr.OFTString)
    fieldSchema.SetWidth(25)
    layer.CreateField(fieldSchema)

    # Point Geometry
    point = ogr.Geometry(ogr.wkbPoint)

    # Create Feature
    feature = ogr.Feature(layer.GetLayerDefn())
    

    for i in tids_df.index:
        point.AddPoint(tids_df.loc[i, "Longitude"], tids_df.loc[i, "Latitude"])
        feature.SetGeometry(point)
        feature.SetField("TIDS_ID", i)
        feature.SetField("Location", tids_df.loc[i, "Location Description"])
        feature.SetField("Latitude", tids_df.loc[i, "Latitude"])
        feature.SetField("Longitude", tids_df.loc[i, "Longitude"])
        layer.CreateFeature(feature)

    dataSource.Destroy()
        


    