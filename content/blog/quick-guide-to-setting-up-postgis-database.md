Title: Quick guide to setting up a PostGIS database
Date: 2008-11-28 12:01
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: PostGIS, Quick Guide, Ubuntu, FOSS, GIS, How-To, Linux
Slug: quick-guide-to-setting-up-postgis-database

Recently I decided to seriously start using PostGIS to manage my spatial
data. As I have several projects on the go, organizing and managing my
data effectively has become extremely important, and PostGIS is by far
the most convenient way to do this. There is lots of documentation out
there that explains in detail how to set up PostGIS, but by far the best
reference I've found is from [Tim Sutton's blog][], mainly because he
uses Ubuntu, and sudo-apt gets everything you need to have PostGIS
working in minutes.
<!--more-->

Here is a [link to the article][], and below is a quote from his blog:

> Another reason I love Ubuntu - getting postgis + postgresql is really easy...

```bash
sudo apt-get install postgis postgresql-8.3-postgis
sudo su postgres
createuser -s -d -r -l -P -E -e timlinux
exit
```

> Enter prompts following above commands as needed. Now you have
> postgres installed and a user created. Next create an empty spatial
> database:

```bash
createdb qgis
createlang plpgsql qgis
psql qgis < /usr/share/postgresql-8.3-postgis/lwpostgis.sql
psql qgis < /usr/share/postgresql-8.3-postgis/spatial_ref_sys.sql
```

> Easy peasy.

[Tim Sutton's blog]: http://tim.linfiniti.com/ "Tim Sutton's blog"
[link to the article]: http://tim.linfiniti.com/page/3 "Setting Up Postgis on Ubuntu"
