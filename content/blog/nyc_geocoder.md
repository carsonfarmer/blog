Title: NYC Geoclient REST API from Python
Date: 2014-02-03 11:40
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Python
Tags: Announcement, Python
Slug: nyc_geocoder
Status: draft

Recently, on the [betaNYC][] Meetup email list, [John Krauss][krauss] and 
[Tom Swanson][swanson] both posted Python code for accessing the [NYC Geoclient 
REST API][rest], which is an awesome resource developed by the [NYC Department 
of Information Technology and Telecommunications][doit] GIS/Mapping unit.

> The Geoclient API is a RESTful web service interface to the NYC Department of City Planning’s Geosupport system developed 
> by the Department of Information Technology and Telecommunications GIS/Mapping unit. Geosupport is a mainframe-based 
> geocoding system used by NYC government. Geosupport provides coordinate and geographic attributes for supported input 
> locations (address, intersection, blockface). Geoclient exposes the most widely used Geosupport functions and provides them 
> in a more intuitive and modern manner.

This is what John has to say about [his code](https://github.com/talos/nyc-geoclient):

> I've been messing around with NYC's geoclient API.  It's quite powerful!  I wrapped the REST calls in a Python module, 
> which is accessible for all on PyPI.  You can check it out here:
> 
> https://github.com/talos/nyc-geoclient
>
>  And the documentation here:
>
> http://nyc-geoclient.readthedocs.org/en/latest/index.html
>
> On a side-note, according to Geoclient, almost 20% of the intersections in the city's own collision statistics releases are 
> ambiguous or invalid.

And this is what Tom has to say [about his](https://github.com/tswanson/NYCParkingGeocode):

> My code is nowhere near as clean as John’s but if might be of interest that I ran ~3millions records through the NYC 
> GeoClient in December.  Overall, the services worked great and was able to make ~1,500 calls per min.  I was geocoding 
> the parking ticket data on nyc open data.
> 
> https://github.com/tswanson/NYCParkingGeocode

Note that you need to [register an app with DoITT][developer] (and sign it up 
for the Geoclient API) then wait a few days before being able to use the API.
So get registered ASAP!

[betaNYC]: http://www.meetup.com/betanyc/
[krauss]: http://blog.accursedware.com/
[swanson]: http://29degreesnorth.blogspot.com/
[rest]: http://developer.cityofnewyork.us/api/geoclient-api-beta
[doit]: http://www.nyc.gov/html/doitt/html/home/home.shtml
[developer]: http://developer.cityofnewyork.us/
