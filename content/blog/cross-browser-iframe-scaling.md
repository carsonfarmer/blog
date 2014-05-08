Title: Cross-browser iframe scaling
Date: 2012-08-06 18:18
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful Tip
Tags: CSS, HTML, iframe, scaling
Slug: cross-browser-iframe-scaling

This is just a quick post to document an annoyance (and solution) that
I've recently discovered when trying to scale a webpage embedded in
another page using an `iframe`. When trying to come up with a nice way
to embed [this page][] inside [this page][1], I found that webkit based
browsers were not behaving as they should. After a lot of fiddling
about, I discovered that the following `css` seems to fix the issues:
```css
#wrap {  
    width: 630px;
    height: 300px;
    padding: 0;
    overflow: hidden;
}
#frame {  
    -ms-zoom: 0.5;
    -ms-transform-origin: 0 0;
    -moz-transform: scale(0.5);
    -moz-transform-origin: 0px 50px;
    -o-transform: scale(0.5);
    -o-transform-origin: 0px 50px;
    -webkit-transform: scale(0.5);
    -webkit-transform-origin: 0 0;
}
#frame {
    width: 1230px;
    height: 530px;
    overflow: hidden;
}
```
Note that if instead of `-ms-zoom` you use `zoom`, webkit browsers seem
to 'double scale' everything, which turned out to be the root of my
problem. With the above tweaks, everything works fine (for now) using
the following `HTML`:

```html
<div id="wrap">
    <iframe id="frame" src="http://www.website.com/"></iframe>
</div>
```

Hopefully this post will save someone (or me in the future) some
frustration and time. The above fix was cobbled together based on
suggestions from [here][] (see answers from `Kip`, `lxs`, and `r3cgm`).

Carson

[this page]: examples/olympic_countries/
[1]: http://www.st-andrews.ac.uk/geoinformatics/
[here]: http://stackoverflow.com/questions/166160/how-can-i-scale-the-content-of-an-iframe
