Title: Research dissemination and interactive visuals
Date: 2012-04-10 22:12
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Visualisation
Tags: D3, Interactive, Javascript, Online Maps, Visualisation, Free open-source software (FOSS), Opinion
Slug: research-dissemination-and-interactive-visuals

One of my goals for this year is to spend more time and effort
developing effective visualisations for my various research projects, in
an effort to make my research more accessible to others. This is one
thing that I think many academics are particularly bad at: letting
others know what they are up to, and why it might be something worth
looking at. In order to avoid this pitfall, I plan to focus on producing
interactive, web-based visuals suitable for a more general audience *in
addition* to more traditional forms of research dissemination such as
journals and conference papers. It is my hope that by doing this, I will
be making my research more readily available to those who might actually
be able to use it, and maybe even create some compelling visualisations
in the process. While I'm not quite ready to start creating full-blown
interactive websites yet, I thought it might be a good idea to start
with something small to get the ball rolling; so I put together an
[upgraded version][] of my [previous map][] of visitors to www.carsonfarmer.com.
<!--more-->

I used the excellent [D3 JavaScript library][] to re-create the visitor
map, this time providing some basic interaction with the data. Most of
the functionality is based on [examples][] from the D3 website, and at
this point, the map is really more of a learning tool than anything. As
in my previous static map, the IP addresses were geocoded using the
[Data Science Toolkit API][] via the [RDSTK R package][], and all data
processing and manipulation was done using R. Additionally, the colour
scheme functionality comes from [slide 25][] of [this presentation][],
and uses the sequential colour palettes from [colorbrewer.org][]. There
are still a few kinks to work out (like how to get the `onmouseout` event
to work properly in Internet Explorer), and tonnes of additional
features and functions could be added, so comments and suggestions are
welcome. Having said that, I think the new version looks quite nice, and
will likely form the basis for more complex visuals as I become more
familiar with Javascipt and various other web-development tools.

[upgraded version]: /examples/visitors/
[previous map]: |filename|because-its-fun-to-map-stuff.md
[D3 JavaScript library]: http://mbostock.github.com/d3/
[examples]: http://mbostock.github.com/d3/ex/
[Data Science Toolkit API]: http://www.datasciencetoolkit.org/
[RDSTK R package]: https://github.com/rtelmore/RDSTK
[slide 25]: http://mbostock.github.com/d3/talk/20111018/#25
[this presentation]: http://mbostock.github.com/d3/talk/20111018/#0
[colorbrewer.org]: http://colorbrewer2.org/
