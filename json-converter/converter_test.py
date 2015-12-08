# Generic JSON to GeoJSON converter

import json

in_file_location = """buildings.json"""
out_file_location = """buildings.txt"""
lat_field_name = 'latitude'
lon_field_name = 'longitude'
json_data = json.load(open(in_file_location))
geojson_result = {"type": "FeatureCollection","features":[]}

with open(out_file_location,'w') as outfile:
    # for each item in the input json file, go through it
    # and build a feature object
    for feature in json_data:
        # feature object template with placeholders for geometry and properties
        feature_obj = {"type":"Feature","geometry":{},"properties":{}}
        # go through each attribute and build a list of attribute/value pairs
        # handle latitude/longitude separately
        for key in feature.keys():
            if key == lat_field_name:
                y = feature[key]
            elif key == lon_field_name:
                x = feature[key]
            else:
                feature_obj['properties'][key] = feature[key]
        # Add the geometry object to the feature, assuming a point and a z value of 0
        feature_obj['geometry'] = {"type":"Point","coordinates":[float(x),float(y),0]}
        # Add the feature object to the list of features
        geojson_result['features'].append(feature_obj)
    # serialize the result
    json.dump(geojson_result,outfile)
