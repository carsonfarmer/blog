Title: Community structure in directed, weighted networks
Date: 2009-10-20 16:24
Author: cfarmer
Email:  carson.farmer@gmail.com
Category: Networks
Tags: Community structure, Directed, Modularity, Networks, Weighted, Helpful tip, Research
Slug: community-structure-in-directed-weighted-networks
Latex:

Many natural and human systems can be represented as networks, including
the Internet, social interactions, food webs, and transportation and
communication flows. One thing that these types of networks have in
common, is that they can each be represented as a series of vertices (or
nodes) and edges (or links). This [blog entry][] presents a nice
description of networks, highlighting the differences between various
network types (directed, undirected, weighted, unweighted, etc.).
<!--more-->

According to [this paper][leicht], many
networks are found to display "community structure", which basically
refers to groupings of vertices where *within*-group edge connections
are more dense than *between*-group edge connections. In order to detect
and delineate these groupings, [Leicht & Newman (2008)][leicht] present a nice "modularity" optimisation algorithm which is
designed to find a "good" division of a network by maximising

$$Q = \frac{1}{2m}s^TB_s,$$

where $s$ is a vector whose elements define which group each node
belongs to, and $\mathbf{B}$ is the so-called modularity matrix, with elements

$$B_{ij} = A_{ij} - \frac{k_{i}^{in} k_{j}^{out}}{m},$$

where $A_{ij}$ is an element in the adjacency matrix $\mathbf{A}$, $k_{i}^{in}$
and $k_{j}^{out}$ are the in- and out-degrees of the vertices, and $m$ is
the total sum of edges in the network. In practice, this can be extended
to directed networks by considering the matrix $\mathbf{B} + \mathbf{B}^T$ (for an
explanation of why this is the case, see [Leicht & Newman][leicht]).

It is relatively straight-forward to extend the above modularity
optimisation algorithm to the case of a weighted network by computing
the modularity matrix using the in- and out-*strength*(see link to blog
post above) of the vertices instead of the degree. This is similar to
the concept presented in [Newman (2004)][newman], and indeed the
theory of the modularity algorithm holds for this more general case
(note that an unweighted network can simply be represented as a weighted
network where the edge weights are all set to 1). As such, our new
modularity matrix can be computed as

$$B_{ij} = A_{ij} - \frac{s_{i}^{in} s_{j}^{out}}{m},$$

where $m = \sum_{i}s_{i}^{in} = \sum_{j} s_j^{out}$, and $s$ represents the vertex
strength. As such, using the above *new* definition of $\mathbf{B}$, the
modularity of a directed, weighted network is computed as

$$Q = \frac{1}{4m}s^{T}(\mathbf{B}-\mathbf{B}^{T})s.$$

My current research uses a modified modularity optimisation algorithm to
compute [functional regions][] for Ireland based on a range of
socio-economic variables. The goal is to provide a consistent framework
for computing functional regions which are comparable across different
countries and/or regions.

C

### References

Leicht, E. A. & Newman, M. E. J. (2008). [Community structure in directed networks][leicht].
*Physical Review Letters*, 100(11), 118703.

Newman, M. E. J. (2004). [Analysis of weighted networks][newman]. *Physical Review E*, 70(5), 056131.

[blog entry]: http://toreopsahl.com/2008/11/28/network-weighted-network/
[leicht]: http://arxiv.org/abs/0709.4500
[newman]: http://arxiv.org/abs/cond-mat/0407503
[functional regions]: http://en.wikipedia.org/wiki/Functional_region
