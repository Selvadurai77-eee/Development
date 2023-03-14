from osgeo import osr
from osgeo import ogr

# Source Projection
srcCord = osr.SpatialReference()
srcCord.SetUTM(17)

# Destination Projection
dstCord = osr.SpatialReference()
dstCord.SetWellKnownGeogCS('WGS84')

# Transformation Object
transCord = osr.CoordinateTransformation(srcCord, dstCord)

# Read Shape file
shapeFile = ogr.Open("E:\Selvadurai\Programming\Python\Projects\Dev\Geo-Development\Input\miami\miami.shp")
layer = shapeFile.GetLayer(0)

# Create New Shapefile
driver = ogr.GetDriverByName("ESRI ShapeFile")
dataSource = driver.CreateDataSource(r"E:\Selvadurai\Programming\Python\Projects\Dev\Geo-Development\Output\reproject_miami.shp")
layer = dataSource.CreateLayer("miami",dstCord)


feature = ogr.Feature(layer.GetLayerDefn())


# Reproject and save to new Shape file
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    geometry = feature.geometry()
    layer.SetGeometry(geometry.Transform(transCord))
    layer.CreateFeature(feature)

dataSource.Destroy()
    
