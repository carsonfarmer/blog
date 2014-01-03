Title: Creating a visitor map using Google Analytics and Leaftlet
Date: 2013-12-20 11:34
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Python
Tags: Helpful tips, Python, Visualization, Mapping
Slug: visitor_map_via_google_analytics_and_leaftlet
Status: draft

Since moving my blog over to [Pelican][pelican], I have slowly been adding new functionality to get things 'just right'. Being a map geek, one of the things that I have been missing is a nice visitors map. There are lots of simple plugins and tools to add one of these automatically to your site, but I figured I'd do it right and implement this myself using [Leaflet][leaflet] and the very nice [Cluster plugin][cluster] to get similar functionality using tools that I know and trust.
The data (approximate site visitor location) comes from [Google Analytics][ga], which I have setup for my site using the following snippet of JavaScript (replacing UA-XXXXX-X with your web property ID):

```html
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-XXXXX-X']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</script>
```

After you have this setup, it's just a matter of waiting until you get enough site traffic to make this a worthwhile mapping exercise... Once the wait is over, its time to grab the data from Google Analytics. I used some information and pointers from this [blog-post][blog-post] to get me started, and set up the query parameters using the [Google Analytics Query Explorer][ga-explorer]. All I really needed were unqiue visits and the locations that they came from, anything else is just bonus information. In the following snippet, "ga:XXXXXXXX" is replaced with the namespaced view ID of the profile from which to request data (see the Query Explorer for details):

```python
import gdata.analytics.client as client
import datetime

today = datetime.date.today()
last = today - datetime.timedelta(days=30)

my_client = client.AnalyticsClient(source="www.mywebsite.com")
token = my_client.client_login(
	"username", 
	"password", 
	source="www.mywebsite.com", 
	service=my_client.auth_service, 
	account_type="GOOGLE",)

account_query = client.AccountFeedQuery()

data_query = client.DataFeedQuery({
	"ids": "ga:XXXXXXXX",
	"dimensions": "ga:city,ga:latitude,ga:longitude,ga:region,ga:country",
	"metrics":"ga:uniqueEvents",
	"start-date": last.strftime("%Y-%m-%d"),
	"end-date": today.strftime("%Y-%m-%d"),
	"max-results": "5000",
	})

feed = my_client.GetDataFeed(data_query)
```

Once you have the above feed, you can grab the relevant data using something like this:

```python
data = [[r.value for r in row.metric] + [r.value for r in row.dimension] for row in feed.entry]
```

With all that in place, I just created a Python script that runs the above code every time I update my site, generating a list of visitor locations over the last month. Since I already had a map as my site's background, I just updated the Leatleft Javascript to add in the visitor locations using the Cluster plugin. The results look something like this (or, assuming I haven't changed things again, just take a look at the background to this page):

[pelican]: ...
[leaflet]: ...
[cluster]: ...
[blog-post]: http://ilian.i-n-i.org/retrieving-google-analytics-data-with-python/
[ga-explorer]: http://ga-dev-tools.appspot.com/explorer/
[ga]: https://developers.google.com/analytics/devguides/collection/gajs/asyncTracking