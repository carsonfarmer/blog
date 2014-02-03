# Script for querying Google Analytics for creating a nice visitors map
# Query based on following parameters, generated using:
# http://ga-dev-tools.appspot.com/explorer/

# Account : carson.farmer
# Property : Carson Farmer
# View (Profile): All Web Site Data
# ids=ga:72662650
# dimensions=ga:city,ga:latitude,ga:longitude,ga:region,ga:country
# metrics=ga:uniqueEvents
# start-date=
# end-date=2013-10-26
# start-index=2013-11-26
# max-results=5000

# A lot of the following code came from:
# http://ilian.i-n-i.org/retrieving-google-analytics-data-with-python/

import gdata.analytics.client as client
import pandas as pd
import datetime
from geopy import geocoders

today = datetime.date.today()
last = today - datetime.timedelta(days=30)

my_client = client.AnalyticsClient(source="www.carsonfarmer.com")
token = my_client.client_login(
	"carson.farmer", 
	"hunter695park", 
	source="www.carsonfarmer.com", 
	service=my_client.auth_service, 
	account_type="GOOGLE",)

# token = my_client.auth_token

account_query = client.AccountFeedQuery()

data_query = client.DataFeedQuery({
	"ids": "ga:72662650",
	"dimensions": "ga:city,ga:latitude,ga:longitude,ga:region,ga:country",
	"metrics":"ga:uniqueEvents",
	"start-date": last.strftime("%Y-%m-%d"),
	"end-date": today.strftime("%Y-%m-%d"),
	"max-results": "5000",
	})

feed = my_client.GetDataFeed(data_query)

data = [[r.value for r in row.metric] + [r.value for r in row.dimension] for row in feed.entry]
df = pd.DataFrame(data, columns=["visits", "city", "lat", "long", "region", "country"], dtype=float)

df.city[df.city=="(not set)"] = ""
df.region[df.region=="(not set)"] = ""
df.country[df.country=="(not set)"] = ""

def combine_places(row):
	city = row.city + ", " if len(row.city) else ""
	region = row.region + ", " if len(row.region) else ""
	if city + region + row.country == "":
		return "Unknown"
	return city + region + row.country

df["title"] = df.apply(combine_places, axis=1)
no_lat_lon = (df.lat == 0) & (df.long == 0)

gn = geocoders.GeoNames(username="cfarmer")

def geocode(s):
	if s == "Unknown":
		# Just place it in the North Atlantic
		return s, (34.597042,-40.808716)
	return gn.geocode(s)

# Keep things in pieces in case of failures
res = [geocode(s) for s in df.title[no_lat_lon]
ser = [pd.Series(s[1]) for s in res]
ddf = pd.DataFrame(ser, index=df[no_lat_lon].index)
ddf.columns = ["lat", "long"]

df.lat[no_lat_lon] = ddf.lat
df.long[no_lat_lon] = ddf.long

json = df[["lat", "long", "title", "visits"]].to_json(orient='values')
json = json.replace("],[","],\n[")
json = json.replace("[[", "[\n[")
json = json.replace("]]", "]\n];")

with open('visitor_locations.js', 'w+') as f:
    f.write('var visitors = ')
    f.write(json)