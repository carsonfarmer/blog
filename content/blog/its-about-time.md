Title: It's about time...
Date: 2011-11-09 12:16
Author: cfarmer
Email:carson.farmer@gmail.com
Category: Announcement
Tags: Announcement, Research, R, Update, Helpful Tip
Slug: its-about-time

Well its been a long time since my last post, but I *do* have a
relatively good reason: I was finishing up my PhD thesis. The good news
is that I'm now done and graduated! I'm hoping I'll have a bit more time
to blog and continue working on side-projects that I had to put on-hold
while finishing up. My plan for the next few months is to finish up here
in Maynooth, (unofficially) start some post-doc work, and finish/get
going on several papers on my PhD research. I'm also going to try to
learn Bayesian statistics, fiddle about with some visualizations I've
been working on, and start getting back into QGIS and Python development
again

In the mean time, I've put together a fun little visualization of my
PhD thesis in the form of a word-cloud.
<!--more-->

[![image][]][wordcloud]

This is actually a pretty rough version, and I suspect there are a few
issues with hyphenated words and things like that; but it does give a
pretty good impression of what my thesis is all about, so I'll leave it
at that for now. For those who might be interested (and for my own
reference), the `R` code to generate this figure is here (requires the
`wordcloud` and `tm` packages):

```r
# read in all the lines as a character vector
lines <- readLines('modified.txt')
head(lines)
library(tm) # text mining package
library(wordcloud)
# create a corpus object
corpus <- Corpus(DataframeSource(data.frame(lines)))
# now start processing the text and removing punctuation etc
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, function(x) removeWords(x, stopwords("english")))
# create a term document matrix (don't really know what that is...)
tdm <- TermDocumentMatrix(corpus)
# convert to matrix
m <- as.matrix(tdm)
# count up re-occuring words
v <- sort(rowSums(m), decreasing=TRUE)
# create dataframe for word cloud
d <- data.frame(word = names(v), freq=v)
png("wordcloud.png", width=1280, height=800)
wordcloud(d$word,d$freq,c(8,.3),2,100,TRUE,.15, vfont=c("sans serif","plain"))
dev.off()
```

I actually got this snippet from [One R Tip A Day][] via [R-bloggers][].

[image]: |filename|/images/wordcloud-300x280.png "Thesis wordcloud"
[wordcloud]: |filename|/images/wordcloud.png

[One R Tip A Day]: http://onertipaday.blogspot.com/2011/07/word-cloud-in-r.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+OneRTipADay+(One+R+Tip+A+Day)
[R-bloggers]: http://www.r-bloggers.com/
