import requests
import json
import sys
def get_list(place_type = "bar", location="39.986111,-75.153340",miles=0.5):
    radius_in_meters = 1600* miles
    json_dic = None
    list_loc = {}
    address = """
    https://maps.googleapis.com/maps/api/place/nearbysearch/json?
    location={1}
    &radius={2}
    &types={0}
    &key=AIzaSyC5jQ1WteY0K74b-NBUJinUgxl0aoy4Hrw
    """.format(place_type,location,radius_in_meters)
    address = "".join(address.split())
    req = requests.get(address)
    if req.status_code == 200:
        json_dic = json.loads(req.text)
    else:
        print(req.status_code)
        sys.exit()
    for item in json_dic['results']:
        list_loc[item["name"]] = item["vicinity"]
    print(list_loc)
    
"""
get_list(place_type="bar")
{'The Hubble Bubble Hookah Lounge': '1000 Diamond Street #118, Philadelphia', 'Temple Student Center': 'Student Center South, 1755 North 13th Street, Philadelphia', 'Howard Gittis Student Center': '1755 North 13th Street, Philadelphia', 'Red Top 24 Bar': '2400 North 16th Street, Philadelphia', "Fang's Restaurant": '2600 North 12th Street, Philadelphia', "Al's Spot": '2540 North 15th Street, Philadelphia'}
>>> get_list(place_type="cafe")
{"McDonald's": '2109 North Broad Street, Philadelphia', 'Starbucks': 'Philadelphia', 'Garvey-Wells Bookstore and Touba Cafe': '2231 North Broad Street, Philadelphia', "Dunkin' Donuts": '2344 North Broad Street, Philadelphia', 'Blazin Flavorz': '2406 Germantown Avenue, Philadelphia', 'Saige Cafe': '1802 North Warnock Street, Philadelphia', 'Saxbys Temple University': '1902 Liacouras Walk, Philadelphia', 'The Rad Dish Co-op Cafe': '1301 Cecil B. Moore Avenue, Philadelphia', 'Lucky Cup Cafe': '2020 North 13th Street, Philadelphia', "The Artist's Pallet Cafe": 'Philadelphia', 'Saxbys Temple Fox': '1810 North 13th Street, Philadelphia', 'Fresh Bytes': 'North 13th Street, Philadelphia', 'Bagel Hut': '1348-, 1360 West Montgomery Avenue, Philadelphia', 'Lucky Cup': '1620 North Broad Street, Philadelphia'}
>>> get_list(place_type="night_club")
{'The Hubble Bubble Hookah Lounge': '1000 Diamond Street #118, Philadelphia', 'Temple Student Center': 'Student Center South, 1755 North 13th Street, Philadelphia', 'Howard Gittis Student Center': '1755 North 13th Street, Philadelphia'}
"""
    
    