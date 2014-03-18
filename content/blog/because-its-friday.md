Title: Because its Friday
Date: 2010-11-06 01:00
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Python
Tags: Multiprocessing, Python, R, Statistics, FOSS
Slug: because-its-friday

My two favorite scientific programming languages are [Python][] and
[R][], each for their own specific strengths. I stick with R for most of
my serious stats stuff, but for everyday processing, analysis, and GUI
building, Python is my *modus operandi*. Lately however, I've been doing
more and more things in Python... even the stats stuff. When doing
statistical analysis in Python, I usually use the excellent [rpy2][]
library to communicate between Python and R. As a result, I have put
together quite a few little code snippets to work with R commands in
Python. Recently, I decided to put a bunch of these snippets together to
create what I've called fakeR. Basically it is a simple Python script
that emulates a very basic (toy) R console. The fakeR console supports
multi-line commands and pretty much all regular R commands, but has no
history or any nice features like that. The cool and/or handy thing
about it is that it separates the input/output from the actual
processing via the very cool [multiprocessing][] Python package. Using
this package, it is possible to separate the input/output and processing
into two separate processes running in parallel, with communication back
and forth done via a duplex (two-way) pipe. I've [uploaded the script][]
for anyone interested in having a play with it. If anyone has any ideas
on how to (safely) cancel a currently running R command on the
processing side, I'd be very interested to hear them.

Carson

[Python]: http://www.python.org
[R]: http://http://www.r-project.org/
[rpy2]: http://rpy.sourceforge.net/rpy2.html
[multiprocessing]: http://docs.python.org/library/multiprocessing.html
[uploaded the script]: |filename|/uploads/faker.py
