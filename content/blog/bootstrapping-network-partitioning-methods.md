Title: Bootstrapping network partitioning methods
Date: 2010-04-17 14:26
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Networks
Tags: Networks, R, Uncertainty, How-to
Slug: bootstrapping-network-partitioning-methods

My PhD research at the moment focuses on network-based algorithms for
delineating functional regions (geographical regions within which a
large majority of the local population seeks employment, and the
majority of local employers recruit their labour). Currently I'm using a
network partitioning algorithm based on [modularity maximisation][]. I
have found my results to be quite good so far, but, 'quite good' isn't
really a very scientific description of validity, so obviously some
others means of validation is required. Enter bootstrap resampling!
<!--more-->

Bootstrapping can be used to assess the **validity** of a
particular network partitioning by measuring the **stability** of the
detected partitions (or clusters). Here, a cluster may be thought of as
stable if, for example, it remains relatively invariant to random- or
sampling-error and noise. In this sense, we're interested in
distinguishing between clusters which reﬂect the true nature of the
dataset, and those generated as a result of random effects, data
uncertainties, or measurement error.

The process works like this:

1. Generate a large number of random 'bootstrap samples' from a
   (directed) weighted network,
2. Apply some network partitioning algorithm to the original network,
3. (Re)apply the network partitioning algorithm to each bootstrap
   sample,
4. For each cluster in the original network partitioning, the most
   similar cluster in each bootstrap replicate is found using the
   [Jaccard coeffcient][] `γ` as a measure of similarity, and
   similarity is recorded,
5. The stability of each cluster is assessed based on the mean Jaccard
   similarity over all resampled datasets.

Once the above process is run, we get an estimate of how stable each
cluster is. We can then use this information to decide which clusters to
keep, and which ones need to be merged with their closest neighbour.
There are several ways to specify how we resample the data. If we assume
no specific structure in the dataset, regular non-parametric bootstrap
resampling will work fine, however, alternative resampling strategies
include: a) replacing network edge weights with noise, b) adding a small
amount of noise to (a percentage of) the network edges, or c) using only
a subset of the original network (i.e., generating a subgraph of the
original network).

I tested this process on a computer generated network with three
predefined clusters using resampling strategy (*`b`*) above, by adding
random noise to *`k`* percent of the network edges, and observed the
effect of increasing levels of uncertainty by applying the resampling
technique to increasing values of *`k`*. The results show just what we
would expect: as more noise is added to the dataset, the stability of
the detected clusters goes down. The nice bit however, is that for
*`k <= 0.5`*, the detected clusters remained relatively stable
(*`γ >= 0.6`*), meaning the network partitioning algorithm I was using
is doing a pretty good job. Nice!

This bootstrapping process is part of a paper I'm working on at the
moment, and uses a geographical variant of [this algorithm][] to detect
functional regions in travel to work data. I'll post more on the
algorithm and my bootstrapping implementation in R (using the very cool
[foreach][] package) here soon.

### References

Leicht, E. A., & Newman, M. E. J. (2008). [Community structure in
directed networks][]. *Physical Review Letters*, 100(11), 118703.

Hennig, C. (2007). [Cluster-wise assessment of cluster stability][].
*Computational Statistics & Data Analysis*, 52(1), 258-271.

[modularity maximisation]: http://en.wikipedia.org/wiki/Modularity_(networks)
[Jaccard coeffcient]: http://en.wikipedia.org/wiki/Jaccard_index
[this algorithm]: {filename}/blog/community-structure-in-directed-weighted-networks.md
[foreach]: http://cran.r-project.org/web/packages/foreach/index.html
[Community structure in directed networks]: http://prl.aps.org/abstract/PRL/v100/i11/e118703
[Cluster-wise assessment of cluster stability]: http://www.sciencedirect.com/science/article/B6V8V-4MJJMV8-1/2/303f8dd772cd73d54aea3a224b188005
