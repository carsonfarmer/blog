Title: manageR and rpy2 installation problems
Date: 2012-10-06 14:26
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful Tip
Tags: Python, QGIS, R, Spatial, FOSS
Slug: manager-and-rpy2-installation-problems

Unfortunately, I haven't had much time recently to update or work on
`manageR`, but I'm hoping that will change in the next few months...
Having said that, there are quite a few people out there that have been
having trouble installing `manageR` (and the required `rpy2`) on their
system to get things working at all! I have had some individuals provide
possible fixes and suggestions on how to get things working properly on
various platforms, and I'm going to use this post to amalgamate them,
and hopefully create a one stop post for all your `rpy2` and `manageR`
needs. I'm also hoping that people will post potential fixes in the
comments to help others with more specific problems?
<!--more-->
For now, I have the following potential fix for `OSX` (Lion 10.7.2 at
least):

1.  Update `R` to latest version ([binary from r-project.org][]);
2.  Reinstall `QGIS` ([Kyngchaos installer][]);
3.  Reinstall `GDAL_complete` ([Kyngchaos again][]);
4.  Reinstall `rpy2` (latter via [pip][])
5.  Reboot...

Apparently the (potential) problem is actually related to previous `R`
builds, where symlinks were referring to the wrong location. This
potential fix is courtesy of [this Stackexchange thread][stackexchange]

Ok, so does anyone else have some suggestions to get things working on
Windows? Perhaps someone out there has a Windows build they'd like to
share? As far as I know (i.e., it works for me), things are working fine
on Linux, but if someone else has a different experience, please share
in the comments.

[binary from r-project.org]: http://www.r-project.org/
[Kyngchaos installer]: http://www.kyngchaos.com/software/qgis
[Kyngchaos again]: http://www.kyngchaos.com/software/frameworks
[pip]: http://rpy.sourceforge.net/rpy2_download.html
[stackexchange]: http://gis.stackexchange.com/questions/17169/is-it-possible-to-run-an-r-script-on-a-layer-in-qgis "Run an R Script on layer in QGIS"
