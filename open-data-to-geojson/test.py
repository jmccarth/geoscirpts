import urllib
import urllib2
import json

api_url = "http://api.uwaterloo.ca/v2/buildings/list.json?key=cb63602dd1fd2a14332405f8613b68ed"
response = urllib2.urlopen(api_url).read()
json_response = json.loads(response_data)
