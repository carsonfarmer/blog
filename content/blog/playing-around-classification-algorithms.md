Title: Playing around with classification algorithms: Python and QGIS
Date: 2010-09-23 10:56
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Python
Tags: Classification, Jenks, Python, QGIS, R, FOSS, GIS
Slug: playing-around-with-classification-algorithms-python-and-qgis

Data visualization is part of my everyday work-flow. More often than
not, I'm playing around with my data in a GIS to tease out interesting
or informative spatial patterns, or to ensure that I'm getting the
results that I'm expecting. As a result, I am constantly trying out
different classification schemes to help me generalize spatial patterns,
highlight outliers and/or patterns, or just plain [mess around with my
data][].
<!--more-->

Unfortunately, [QGIS][] (which has been my primary GIS for several years
now) only <strike>has</strike> had 'Equal Interval' and 'Quantiles' classification algorithms
implemented. While these classification schemes are no doubt useful and
revealing when used in the right context, I often need something that
better represents the 'actual' distribution of values in my data. For
this, I usually turn to the [Jenks Optimisation][] (or Natural Breaks)
classification. Essentially, this classification algorithm generates
class intervals that minimize within group variance, and maximize
between group variance. In this way, given a certain number (`k`) of
classes, we arrive at an 'optimal' classification of our data into `k`
classes. In the past, I would import my data into [R][], and calculate
class intervals using the very handy [classInt][] package. However,
moving data between QGIS and R, while slightly easier using my [manageR
tool][] (shameless plug!), is not optimal when all I really want to do
is fiddle around with different classification schemes. So I decided to
reimplement the Jenks algorithm in Python so that I could do things
directly from the Python console in QGIS.

Obviously I didn't really want to implement this algorithm from scratch,
so I had a look at the R code from the `classInterval` function in the
classInt package (ah open source!), as well as the handy Python script
[from here][]. Once I had the code in hand, it didn't take long to have
a nice Python script ready to be run on my data directly from within
QGIS. While I was at it, I also implemented a few other classification
algorithms to play around with, including 'Equal Interval', 'Quantiles',
'Standard Deviation', and R's 'Pretty' algorithm. For those of you who
don't know, R's pretty algorithm basically computes a sequence of about
'n+1' equally spaced 'round' values which cover the range of our input
data, such that the class breaks are 1, 2 or 5 times a power of 10. The
Python script is [available here][], and has a version of the pretty
algorithm based on code from the [labeling][] package.

[mess around with my data]: http://www.markmonmonier.com/how_to_lie_with_maps_14880.htm
[QGIS]: http://www.qgis.org/
[Jenks Optimisation]: http://en.wikipedia.org/wiki/Jenks_Natural_Breaks_Optimization
[R]: http://www.r-project.org/
[classInt]: http://cran.r-project.org/web/packages/classInt/index.html
[manageR tool]: http://code.google.com/p/ftools-qgis/
[from here]: http://danieljlewis.org/2010/06/07/jenks-natural-breaks-algorithm-in-python/
[available here]: |filename|/uploads/class_intervals.py
[labeling]: https://r-forge.r-project.org/projects/labeling/
