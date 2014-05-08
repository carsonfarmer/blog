Title: Aspect Ratio for Plotting Long & Lat
Date: 2014-04-03 12:00
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Visualization
Tags: Python, R, FOSS4G, Helpful Tip, GIS
Slug: aspect_ratio_plotting_long_lat
Status: draft

Here's some `R` code to do it:
```{r}
require(rgdal)
poly = spTransform(poly, CRS("+init=epsg:4326"))
plot(poly)
axis(1)
axis(2)
```
Looks okay, right? The aspect ratio isn't 1 here.

What is it? Well, on the equator it would be 1,  and simple trig will
suggest it goes with the inverse of the cosine of the latitude. What's the
middle of your data?
```{r}
bb = bbox(polyL)
bb
         min        max
x -122.76891 -119.09532
y   51.42396   53.94661

mean(bb[2,])
[1] 52.68528
```
so the ratio is:
```{r}
rat = 1/cos(52.68*pi/180)
rat
[1] 1.649441
```

then:
```{r}
ggplot(polyL) +
  aes(long,lat,group=group, fill = id) +
  geom_polygon() +
  geom_path(color="white") +
  coord_fixed(ratio=rat)
```

Since I love Python, here's the Python code to do the same thing:
<!--more-->
