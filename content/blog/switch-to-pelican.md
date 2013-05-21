Title: Making the switch to Pelican
Date: 2013-05-12 11:16
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Announcement
Tags: Announcement, Pelican, Blog, Update
Slug: making-the-switch-to-pelican

Welcome to the new and improved `carsonfarmer.com`! If you are reading this, then
you are enjoying my new, responsive static website/blog. The new site is powered 
by [Pelican][pelican] -- a static website generator written in Python -- and is hosted 
on [GitHub][github] using [GitHub Pages][gh-pages]. Most of the content on the 
site is written in Markdown, which makes it really easy to add headings, anchors, 
and all sorts of goodies to simplify writing blog posts and web-pages.
<!--more-->

The move from WordPress to Pelican was relatively painless, though there were
some issues with comments and converting (some) existing posts to Markdown. I
also took the opportunity to update the site, change the page structure a bit
and try out a few things like adding icons ([FontAwesome][font-awesome]), using 
Twitter [Bootstrap][bootstrap] for some of the UI, and some other tweaks. To get 
me though the process, I took advantage of several blogs and sites dedicated to 
documenting the switch to Pelican:

* [Pelican documentation][pelican-docs] (which is great)
* [Creating A Pelican-Powered Site on GitHub Pages][magically-us]
* [Pelican Guide - Moving From WordPress and Initial Setup][pelican-guide]
* [Yes, this blog is now powered by Pelican][powered-by-pelican]

Once I get things working, I'll also start to think about some of the 
[points here], to make things even _more_ responsive and readable.

<p class="note right shadow">
One of the things that I did have trouble with was getting my RSS feeds set 
up like it was in my WordPress site: /?feed=rss2.
For now, I'm just rerouting things to /feeds/all.rss.xml, but search engines 
won't recognize this, and I'm sure there is a better solution out there... any 
thoughts?
</p>
I am still missing some things that WordPress did quite nicely, including
comments (I'm now relying on [Disqus][disqus] for comments), site search (I've 
started using [Tapir][tapir] for this, and have implemented a cool search tool 
that I may turn into a Pelican plug-in if I find some time), and the plethora of 
plug-ins and themes available for WordPress sites. Having said that, it *is* 
relatively easy to create new themes, and adding social networking components 
like a Twitter Feed using standard html is pretty simple. 

[font-awesome]: http://fortawesome.github.io/Font-Awesome/
[pelican]: http://blog.getpelican.com/
[github]: https://github.com/
[gh-pages]: http://pages.github.com/
[bootstrap]: http://twitter.github.io/bootstrap/
[magically-us]: http://magically.us/2013-02-03/creating-a-pelican-powered-site-on-github-pages.html
[pelican-docs]: http://docs.getpelican.com/
[points here]: http://arunrocks.com/moving-blogs-to-pelican/
[powered-by-pelican]: http://blog.aclark.net/2012/09/21/yes-this-blog-is-now-powered-by-pelican/
[pelican-guide]: http://www.macdrifter.com/2012/08/pelican-guide-moving-from-wordpress-and-initial-setup.html
[disqus]: http://disqus.com/
[tapir]: http://tapirgo.com/

