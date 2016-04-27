import urllib
import urllib2
import json
import os

out_files_directory = """."""
api_token = "cb63602dd1fd2a14332405f8613b68ed"
urls = {
    "buildings":"http://api.uwaterloo.ca/v2/buildings/list.geojson",
    "accessible_entrances": "http://api.uwaterloo.ca/v2/poi/accessibleentrances.geojson"
}
responses = {}
for layername, url in urls.items():
    api_url = url + "?key=" + api_token
    response = urllib2.urlopen(api_url).read()
    resp = json.loads(response)
    out_file_location = out_files_directory + os.path.sep + layername + ".json"
    with open(out_file_location,'w') as outfile:
        json.dump(resp, outfile)
