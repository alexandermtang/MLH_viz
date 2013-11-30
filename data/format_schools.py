import csv
import json
import urllib
import urllib2
import time

schools = []
res_schools = []

with open('schools.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        schools.append(row[0])
    schools = schools [1:] # Remove first 'School' entry

for school in schools:
    url = "http://maps.googleapis.com/maps/api/geocode/json"
    data = {'address': school,
            'sensor': 'false'}
    values = urllib.urlencode(data)
    req = url + '?' + values
    #print full_url

    time.sleep(0.3)
    raw_res = urllib2.urlopen(req).read()
    res_json = json.loads(raw_res)

    status = res_json['status']
    if status == "OVER_QUERY_LIMIT":
        print "Failed on school: %s" % school

    results = res_json['results'][0]
    #print json.dumps(results, indent=2, sort_keys=True)

    state = ""
    country = ""
    city = ""
    lat, lng = 0, 0

    for comp in results['address_components']:
        if 'administrative_area_level_1' in comp['types']:
            state = comp['short_name'].encode('utf-8')
        if 'country' in comp['types']:
            country = comp['short_name'].encode('utf-8')
        if 'locality' in comp['types']:
            city = comp['short_name'].encode('utf-8')
    lat = results['geometry']['location']['lat']
    lng = results['geometry']['location']['lng']

    print [school, city, state, country, lat, lng]
    res_schools.append([school, city, state, country, lat, lng])

with open('universities.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for school in res_schools:
        writer.writerow(school)
