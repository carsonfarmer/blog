Title: Google Summer of Code 2014
Date: 2014-05-08 11:18
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Annoucement
Tags: Annoucement, Coding, Visualization, FOSS4G, Sustainability
Slug: google-summer-of-code-2014
Status: draft

[![Chord flow diagram with time slider][image]{.right}][viz] 

I recently attended the April 2014 [#BetaNYC][beta-nyc] (#BikeNYC) [@CitiBikeNYC][citi-bike-twitter] Hacknight, and after seeing several interesting presentations on what people *are* doing, *want* to be doing, and are *thinking* of doing with the recently released [Citi Bike Trip Histories][citi-bike-data], I was inspired. A few of us got together to 'quickly' and 'easily' hack together a [Sankey diagram][sanky] of the bike trip flows... Turns out this wasn't nearly as quick and easy as we though: By the end of the evening, we were still struggling with getting [D3js][d3js]'s [Sankey][d3-sanky] plugin to play nicely with our data (which I was manipulating in Python using [Pandas][pandas]). I ended up playing around with the data later, and opted to visualize the flows between [NYC neighborhoods][neighborhoods] using a simpler [chord diagram][chord-layout].

A chord diagram arranges the nodes (neighborhoods) radially, drawing thick curves between nodes. In my version, the thickness of links between neighborhoods encodes the relative frequency of rides between two neighborhoods: thicker links represent more frequent rides. Only flows that represent more than 1000 trips are represented to avoid too many small flows. Links are directed, and are colored by the more frequent origin (i.e., colored according to where most of the trips originate from). Whereas thecColors themselves are pretty much arbitrary.

The [visualization is here][viz], and you can move the slider around to change which year/month is shown. Play around by sliding around and comparing flows over different time periods. Also watch for chord 'flipping', where the dominant flow direction changes from month to month. This is particularly common in the smaller flows, where there isn't a strong dominant direction.

The whole thing was built using [D3js][d3js] and based very heavily on [this](http://bost.ocks.org/mike/uberdata), [this](http://exposedata.com/tutorial/chord/latest.html), and [this](http://fleetinbeing.net/d3e/chord.html). As I mentioned, the initial visualization was started at the April 2014 #BetaNYC Hacknight, and the version [linked here][viz] is what I ended up with. Checkout the linked visualization for details on the data sources and the actual code/data used to produce it.


[beta-nyc]: http://www.meetup.com/betanyc/
[citi-bike-twitter]: https://twitter.com/CitibikeNYC
[citi-bike-data]: https://citibikenyc.com/system-data
[sanky]: http://bost.ocks.org/mike/sankey/
[d3js]: http://d3js.org/
[d3-sanky]: https://github.com/d3/d3-plugins/tree/master/sankey
[pandas]: http://pandas.pydata.org/
[chord-layout]: https://github.com/mbostock/d3/wiki/Chord-Layout
[neighborhoods]: http://nycdata.pediacities.com/dataset?tags=neighborhoods
[viz]: http://bl.ocks.org/cfarmer/11478345
[image]: {filename}/images/chord_citibike.png