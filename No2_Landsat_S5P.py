import ee 
from ee_plugin import Map 

# I. PROJECT__DATA_SETS:
# Landsat8_DATA_SET:
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']

# Landsat8_2019
landsat8_2019 = l8.filterBounds(geom) \
                  .filterDate("2018-12-01", "2019-12-31") \
                  .filterMetadata("CLOUD_COVER", "less_than", 1) \
                  .select(bands) \
                  .mean()
Map.addLayer(landsat8_2019, {'bands': ["B4",  "B3",  "B2"], 'min':0, 'max': 0.3}, "RGB")

# Landsat8_2018
landsat8_2018 = l8.filterBounds(geom) \
                  .filterDate("2018-01-01", "2018-12-31") \
                  .filterMetadata("CLOUD_COVER", "less_than", 1) \
                  .select(bands) \
                  .mean()
Map.addLayer(landsat8_2018, {'bands': ["B4",  "B3",  "B2"], 'min':0, 'max': 0.3}, "RGB")

# Landsat8_2017
landsat8_2017 = l8.filterBounds(geom) \
                  .filterDate("2017-01-01", "2017-12-31") \
                  .filterMetadata("CLOUD_COVER", "less_than", 1) \
                  .select(bands) \
                  .mean()
Map.addLayer(landsat8_2017, {'bands': ["B4",  "B3",  "B2"], 'min':0, 'max': 0.3}, "RGB")

# Landsat8_2016
landsat8_2016 = l8.filterBounds(geom) \
                  .filterDate("2016-01-01", "2016-12-31") \
                  .filterMetadata("CLOUD_COVER", "less_than", 1) \
                  .select(bands) \
                  .mean()
Map.addLayer(landsat8_2017, {'bands': ["B4",  "B3",  "B2"], 'min':0, 'max': 0.3}, "RGB")

# Landsat8_2015
landsat8_2015 = l8.filterBounds(geom) \
                  .filterDate("2015-01-01", "2015-12-31") \
                  .filterMetadata("CLOUD_COVER", "less_than", 1) \
                  .select(bands) \
                  .mean()
Map.addLayer(landsat8_2015, {'bands': ["B4",  "B3",  "B2"], 'min':0, 'max': 0.3}, "RGB")



# TROPOMI_DATA_SET
# TROPOMI_2019:
tropomi_2019 = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2') \
  .select('tropospheric_NO2_column_number_density') \
  .filterDate('2019-01-01', '2019-12-31') \
  .mean()
band_viz = {
  'min': 0,
  'max': 0.0002,
  'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}
print('Raw pixel value: ', tropomi_2019)
Map.addLayer(tropomi_2019, band_viz, 'S5P N02')

# TROPOMI_2018:
tropomi_2018 = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2') \
  .select('tropospheric_NO2_column_number_density') \
  .filterDate('2018-01-01', '2018-12-31') \
  .mean()
band_viz = {
  'min': 0,
  'max': 0.0002,
  'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}
print('Raw pixel value: ', tropomi_2018)
Map.addLayer(tropomi_2018, band_viz, 'S5P N02')




# II. CREATING TRAINING DATA SET:
randomSamples
toList_geom = ee.List([
          h1,
          h2,
          h3,
          m1,
          m2,
          m3,
          l1,
          l2,
          l3,
])
# Map over a list equal to the amount of geometries

def func_yro(i):
  # get the geometry corresponding to the number
  pasto = ee.Geometry(toList_geom.get(ee.Number(i)))
  # make random samples. Map over the collection to give each feature a class name
  randomSamples = ee.FeatureCollection.randomPoints(toList_geom.get(i),400).map(function(feat){
      return feat.set('Class', i)
    })
  return randomSamples
# return the flattened collection of collections

FeatCol = ee.FeatureCollection(ee.List.sequence(0, toList_geom.length().subtract(1)).map(func_yro
)).flatten()








)).flatten()
# print limited to 5000 otherwise it won't print
print(FeatCol.limit(5000))
#Map.addLayer(FeatCol, {}, 'Class')

# ----------------------------------------------------------------------


# III. Apply Classification Methods
# Random Forest Classification:
# Sample the input imagery to get a FeatureCollection of training data.
training = landsat8_2019.select(bands).sampleRegions({
               'collection': FeatCol,
               'scale': 30
})
print("Training points", training)

# Filter out the {} property values and try again.
trainingNoNulls = training.filter(
  ee.Filter.NotNull(training.first().propertyNames())
)
print("Training points_NoNull", trainingNoNulls)

#--------------------------------------------
# Export the FeatureCollection to a KML file.
Export.table.toDrive({
  'collection': trainingNoNulls,
  'description':'vectorsToKML',
  'fileFormat': 'KML'
})
# Export the FeatureCollection to a CSV file.
Export.table.toDrive({
  'collection': trainingNoNulls,
  'description':'vectorsToCSV',
  'fileFormat': 'CSV'
})
# ------------------------------------------------

# Make a Random Forest classifier and train it.
classifier = ee.Classifier.smileRandomForest(100) \
    .train({
      'features': trainingNoNulls,
      'classProperty': 'Class',
      'inputProperties': bands
    })

# Classify the input imagery.
classified = landsat8_2019.select(bands).classify(classifier)
Map.addLayer(classified, {'min': 1, 'max': 9, 'palette': ['red', 'pink', 'orange', 'yellow', 'blue', 'teal', 'purple', 'violet', 'green']}, 'classification')
print(classified)

#--------------------------------------------------------

# IV. VALIDATION OF CLASSIFICATION:
# Get Validation Points
randomSamplesV
toList_geomV = ee.List([
          h1V,
          h2V,
          h3V,
          m1V,
          m2V,
          m3V,
          l1V,
          l2V,
          l3V,
])
# Map over a list equal to the amount of geometries

def func_iqz(i):
  # get the geometry corresponding to the number
  pastoV = ee.Geometry(toList_geomV.get(ee.Number(i)))
  # make random samples. Map over the collection to give each feature a class name
  randomSamplesV = ee.FeatureCollection.randomPoints(toList_geomV.get(i),200).map(function(feat){
      return feat.set('Class', i)
    })
  return randomSamplesV
# return the flattened collection of collections

FeatColV = ee.FeatureCollection(ee.List.sequence(0, toList_geomV.length().subtract(1)).map(func_iqz
)).flatten()








)).flatten()
# print limited to 5000 otherwise it won't print
print(FeatColV.limit(5000))
#Map.addLayer(FeatColV, {}, 'Class')

# Classification accuracy
# Get a confusion matrix representing resubstitution accuracy.
trainAccuracy = classifier.confusionMatrix()
print('Resubstitution error matrix: ', trainAccuracy)
print('Training overall accuracy: ', trainAccuracy.accuracy())
validation = classified.sampleRegions({
  'collection': FeatColV,
  'properties': ['Class'],
  'scale': 30,
})
print(validation)
# Compare validation data againts the classification result
testAccuracy = validation.errorMatrix('Class', 'classification')
# Print the error matrix to the console
print('Validation error matrix:', testAccuracy)
# Print the overal accuracy to the console
print('Validation overal accuracy:', testAccuracy.accuracy())
#------------------------------------------------------------------





