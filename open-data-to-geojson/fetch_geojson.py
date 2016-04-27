import urllib
import urllib2
import json
import os

out_files_directory = """."""
api_token = "cb63602dd1fd2a14332405f8613b68ed"
urls = {
    "buildings":"http://api.uwaterloo.ca/v2/buildings/list.geojson",
    "accessible_entrances": "http://api.uwaterloo.ca/v2/poi/accessibleentrances.geojson",
    "food_services": "http://api.uwaterloo.ca/v2/foodservices/locations.geojson",
    "atms": "http://api.uwaterloo.ca/v2/poi/atms.geojson",
    "greyhound": "http://api.uwaterloo.ca/v2/poi/greyhound.geojson",
    "helplines": "http://api.uwaterloo.ca/v2/poi/helplines.geojson",
    "libraries": "http://api.uwaterloo.ca/v2/poi/libraries.geojson",
    "photospheres": "http://api.uwaterloo.ca/v2/poi/photospheres.geojson",
    "defibrilators": "http://api.uwaterloo.ca/v2/poi/defibrilators.geojson",
    "construction_sites": "http://api.uwaterloo.ca/v2/poi/constructionsites.geojson",
    "visitor_information": "http://api.uwaterloo.ca/v2/poi/visitorinformation.geojson",
    "parking_visitor": "http://api.uwaterloo.ca/v2/parking/lots/visitor.geojson",
    "parking_meter": "http://api.uwaterloo.ca/v2/parking/lots/meter.geojson",
    "parking_permit": "http://api.uwaterloo.ca/v2/parking/lots/permit.geojson",
    "parking_shortterm": "http://api.uwaterloo.ca/v2/parking/lots/shortterm.geojson",
    "parking_accessible": "http://api.uwaterloo.ca/v2/parking/lots/accessible.geojson",
    "parking_motorcycle": "http://api.uwaterloo.ca/v2/parking/lots/motorcycle.geojson",
    "grt": "http://api.uwaterloo.ca/v2/transit/grt/stops.geojson"
}
responses = {}
for layername, url in urls.items():
    api_url = url + "?key=" + api_token
    response = urllib2.urlopen(api_url).read()
    resp = json.loads(response)
    out_file_location = out_files_directory + os.path.sep + layername + ".json"
    with open(out_file_location,'w') as outfile:
        json.dump(resp, outfile)
