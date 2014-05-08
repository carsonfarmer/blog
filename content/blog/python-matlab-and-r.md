Title: Python, Matlab, and R
Date: 2009-08-12 15:29
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful Tip
Tags: Matlab, Python, R, FOSS
Slug: python-matlab-and-r

One project I'm working on at the moment involves exploring a dynamic
extension of the Isomap algorithm for visualising constantly varying
real-world road networks. Currently, we are testing out the method on a
small scale simulated road network, and most of the original code
(written by [Laurens van der Maaten][], with updates by [Alexei
Pozdnoukhov][]), was done in Matlab. Since this work is eventually going
to have to run on relatively large datasets, and probably behind the
scenes on a server somewhere, we decided that Python was the way to go.
The goal therefore was to reproduce the Matlab code using only Python
libraries, and the fewer additional libraries required, the better.
<!--more-->

The most difficult stage in all this was to convert the Matlab code to
Python code, while still remaining relatively fast and simple. The
solution is of course the NumPy Python library, and nothing could have
made this conversion more simple than this [pdf document][]. It is
basically a syntax conversion chart between Matlab/Octave, Python, and
R... brilliant!

Check out Vidar Bronken Gundersen's [Mathesaurus][] site for this, and
other useful resources for converting between different mathematical
computation environments.

[Laurens van der Maaten]: http://ticc.uvt.nl/~lvdrmaaten/Laurens_van_der_Maaten/Home.html
[Alexei Pozdnoukhov]: http://ncg.nuim.ie/ncg/people/staff/pozdnoukhov/index.shtml
[pdf document]: |filename|/uploads/matlab-python-xref.pdf
[Mathesaurus]: http://mathesaurus.sourceforge.net/
