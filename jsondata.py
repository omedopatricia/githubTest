from itertools import count
import json
import urllib.request
import json

def  printResults(data):
    #use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    #access json contents
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata', 'title'])

    #output events information
    count = theJSON['metadata']['count']
    print(str(count) + "events receorded")

    #print the places they occurred
    for i in theJSON['features']:
        print(i['properties']['place'])
    print("-------------\n")

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"

    #open the url and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))

    if (webUrl.getcode == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, can't parse results.")

if __name__ == "__main__":
    main()