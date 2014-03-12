Title: A quick bookmarklet for off-campus library access
Date: 2013-12-17 14:56
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: Helpful tip, HTML, Research, How to
Slug: bookmarklet_for_off_campus_library_access

I have been doing a fair bit of research off-campus lately, and as usual, have been having trouble accessing research materials (mainly academic publications) from home. _Fortunately_, Hunter College provides [off-campus access][access-home] to all electronic resources available to Hunter students, faculty and staff via their Library proxy server. _Unfortunately_, it turns out to be a huge pain to use anything other than the library search facilities (like [Google Scholar][scholar]) through the proxy server*. In fact, when working off-campus, you actually have to preface each URL address to licensed resources with 
`http://proxy.wexler.hunter.cuny.edu/login?url=` in order to be able to access it. Not very handy...

[Bookmarklets][bookmarklet] to the rescue! This problem is actually something that bookmarklets are perfect for. A bookmarklet is (usually) just a small piece of JavaScript that resides in your browser and provides additional functionality to a web page. With that in mind, I decided to create a simple bookmarklet to automatically reload a given page with the above prefix prepended to the URL; giving me access to the material via the library proxy server, while still being able to use whatever search tools I want. In this case, all the bookmarklet contains is the following JavaScript code:
```javascript
javascript: location.href="http://proxy.wexler.hunter.cuny.edu/login?url="+location.href
```
So that the whole link is simply:
```html
<a href="javascript: location.href='http://proxy.wexler.hunter.cuny.edu/login?url='+location.href">Library Proxy</a>
```
'Installing' a bookmarklet is as simple as dragging it onto your browser's bookmarks toolbar (I think on some versions of Internet Explorer, you might have to right-click and select "Add to Favorites..."). If you drag this [Library Proxy][proxy] link onto your bookmarks bar, you'll have a handy little tool to automatically access the current page via the Hunter College library proxy (note that you'll need Hunter College credentials for this to work), instantly increasing your productivity by 12.45%... or so.

_*_ I might just be missing something, in which case, hopefully someone will correct me.

[access-home]: http://library.hunter.cuny.edu/find/accessfromhome
[bookmarklet]: http://en.wikipedia.org/wiki/Bookmarklet
[scholar]: http://scholar.google.com/
[proxy]: javascript:location.href='http://proxy.wexler.hunter.cuny.edu/login?url='+location.href