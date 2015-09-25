import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools
import argparse
import datetime
import pandas as pd
import os.path
import sys

today = datetime.date.today()
last = today - datetime.timedelta(days=30)

try:
    file_time = os.path.getmtime('../content/extras/visitors_map.js')
    file_date = datetime.datetime.fromtimestamp(file_time).date()
    if today == file_date:
        print("Already computed map for today... exiting!")
        sys.exit()  # No need to do anything, we've already done this today!
except OSError:  # File doesn't exist!
    pass  # Just pass through, we need to create it...

CLIENT_SECRETS = '~/Documents/client_secrets.json'
# The Flow object to be used if we need to authenticate.
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/analytics.readonly',
    message='%s is missing' % CLIENT_SECRETS
)
# A file to store the access token
TOKEN_FILE_NAME = '~/Documents/credentials.dat'


def prepare_credentials():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()
    # Retrieve existing credendials
    storage = Storage(TOKEN_FILE_NAME)
    credentials = storage.get()
    # If no credentials exist, we create new ones
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)
    return credentials


def initialize_service():
    # Creates an http object and authorize it using
    # the function prepare_creadentials()
    http = httplib2.Http()
    credentials = prepare_credentials()
    http = credentials.authorize(http)
    # Build the Analytics Service Object with the authorized http object
    return build('analytics', 'v3', http=http)

params = {
    "ids": "ga:72662650",
    "dimensions": "ga:city,ga:latitude,ga:longitude,ga:region,ga:country",
    "metrics": "ga:uniqueEvents",
    "start_date": last.strftime("%Y-%m-%d"),
    "end_date": today.strftime("%Y-%m-%d"),
    "max_results": "5000",
}


# Simple function to combine place names
def combine_places(row):
    city = row.city + ", " if len(row.city) else ""
    region = row.region + ", " if len(row.region) else ""
    if city + region + row.country == "":
        return "Unknown"
    return city + region + row.country

service = initialize_service()
data = service.data().ga().get(**params).execute()
# Drop everything that has any field not set...
rows = [row for row in data["rows"] if "(not set)" not in row]
df = pd.DataFrame(rows, columns=["city", "lat", "long", "region",
                                 "country", "visits"], dtype=float)


df["title"] = df.apply(combine_places, axis=1)

json = df[["lat", "long", "title", "visits"]].to_json(orient='values')
json = json.replace("],[", "],\n[")
json = json.replace("[[", "[\n[")
json = json.replace("]]", "]\n];")

with open('../content/extras/visitors_map.js', 'w+') as f:
    f.write('var visitors = ')
    f.write(json)
