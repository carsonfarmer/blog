Title: Event Detection
Date: 2014-03-23 12:00
Author: cfarmer
Slug: presentations/scipy2014
Icon: fa-twitter
Status: hidden
Template: full_page


<script src="http://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.14/require.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2/js/reveal.js"></script>

<!-- General and theme style sheets -->
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2/css/reveal.css">
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2/css/theme/simple.css" id="theme">

<!-- For syntax highlighting -->
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2/lib/css/zenburn.css">

<!--[if lt IE 9]>
<script src="reveal.js/lib/js/html5shiv.js"></script>
<![endif]-->

<!-- Get Font-awesome from cdn -->
<!-- <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css"> -->

    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
html {
  overflow-y: auto;
}
.reveal {
  font-size: 160%;
}
.reveal pre {
  width: inherit;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);
}
.reveal section img {
  border: 0px solid black;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0);
}
/*.reveal i {
  font-style: normal;
  font-family: FontAwesome;
  font-size: 2em;
}*/
.reveal .slides {
  text-align: left;
}
.reveal.fade {
  opacity: 1;
}
.reveal .progress {
  position: static;
}
div.input_area {
  padding: 0.06em;
}
div.code_cell {
  background-color: transparent;
}
div.prompt {
  width: 11ex;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  text-align: right;
}
div.output_area pre {
  font-family: monospace, sans-serif;
  font-size: 80%;
}
div.output_prompt {
  /* 5px right shift to account for margin in parent container */
  margin: 5px 5px 0 0;
}
.rendered_html p {
  text-align: inherit;
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="../../examples/custom.css">

<div class="reveal">
<div class="slides">
<section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="light-weight-real-time-event-detection-with-python">Light-weight real-time event detection with Python</h1>
<p>Carson J. Q. Farmer</p>

<p><i class="fa fa-twitter fa-fw"></i><a href="http://www.twitter.com/carsonfarmer">@carsonfarmer</a><br/>
<i class="fa fa-globe fa-fw"></i><a href="http://www.carsonfarmer.com">carsonfarmer.com</a><br/>
<i class="fa fa-envelope-o fa-fw"></i><a href="mailto:carsonfarmer@gmail.com">carsonfarmer@gmail.com</a><br/>
<i class="fa fa-github-alt fa-fw"></i><a href="https://github.com/cfarmer">github.com/cfarmer</a><br/><br/>
<i class="fa fa-briefcase fa-fw"></i><a href="http://www.hunter.cuny.edu/">Hunter College, City University of New York</a><br/>
<i class="fa fa-map-marker fa-fw"></i><a href="https://www.google.com/maps/place/695+Park+Ave/@40.7687069,-73.9646646,17z/data=!3m1!4b1!4m2!3m1!1s0x89c258ebe705050b:0x22944b98e1be49b7">695 Park Ave, New York, NY, 10065</a></p>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="social-information-sources">Social information sources</h1>
<p><br/>
<br/>
<br/>
<br/></p>
<div style="margin: auto auto; width: 100%; text-align: center;">
    <h2>
        <i class="fa fa-facebook-square fa-4x fa-fw"></i>
        <i class="fa fa-twitter-square fa-4x fa-fw"></i><br/>
        <i class="fa fa-instagram fa-4x fa-fw"></i>
        <i class="fa fa-flickr fa-4x fa-fw"></i>
    </h2>
</div>
</div>
</div>
</div><aside class="notes">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Real-time feeds of user activity from various apps such as Twitter, Foursquare, and others are becoming increasingly available.</p>
</div>
</div>
</div>
    </aside></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/digital_walk.jpg" alt="Digital Traces">
</div>

<p>Source: <a href="http://nmaesthetics.blogspot.com/2011/12/digiself_06.html">Digiself</a></p>
</div>
</div>
</div><aside class="notes">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>These &#39;digital footprints&#39; provide new means to understand how individuals utilize the places and spaces of urban environments.</p>
</div>
</div>
</div>
    </aside></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-what-is-going-on-and-when-and-where-is-it-happening"><em>What</em> is going on, and <em>when</em> and <em>where</em> is it happening</h1>
<p><br/>
<br/></p>
<div style="margin: auto auto; width: 100%; text-align: center;">
    <h2>
        <i class="fa fa-question fa-5x fa-fw"></i> 
        <i class="fa fa-clock-o fa-5x fa-fw"></i> 
        <i class="fa fa-map-marker fa-5x fa-fw"></i>
    </h2>
</div>
</div>
</div>
</div><aside class="notes">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The goal of this work is to provide city planners and others with information on <em>what</em> is going on, and <em>when</em> and <em>where</em> it is happening.</p>
</div>
</div>
</div>
    </aside></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/giscience.png" alt="Digital Traces">
</div>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="streaming-framework">Streaming framework</h1>
<p><br/>
<br/></p>
<div style="margin: auto auto; width: 100%; text-align: center;">
<h2>
    <i class="fa fa-clock-o fa-5x fa-fw"></i>
    <i class="fa fa-leaf fa-5x fa-fw"></i>
</h2>
</div>
</div>
</div>
</div><aside class="notes">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Traditionally, this type of analysis would require a large investment in heavy-duty computing infrastructure, however, we suggest that a focus on real-time analytics in a lightweight streaming framework is the most logical step forward.</p>
</div>
</div>
</div>
    </aside></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/hard_point.jpg" alt="Digital Traces">
</div>

<p>Source: <a href="http://nmaesthetics.blogspot.com/2011/12/digiself_06.html">Digiself</a></p>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="so-what-are-we-doing-">So what are we doing?</h1>
<p><br/>
<br/></p>
<div style="float: left; width: 400px;">
    <ul class="fa-ul" style="list-style: none;">
        <li><i class="fa-li fa fa-twitter fa-fw"></i>Stream Twitter data (location-based)</li>
        <li><i class="fa-li fa fa-quote-right fa-fw"></i>Online Latent Semantic Analysis</li>
        <li><i class="fa-li fa fa-th fa-fw"></i>Gridded count of geo-tweets</li>
        <li><i class="fa-li fa fa-cogs fa-fw"></i>Kernel density estimation (KDE)</li>
        <li><i class="fa-li fa fa-bar-chart-o fa-fw"></i>Normalize tweet density</li>
        <li><i class="fa-li fa fa-search fa-fw"></i>Identify high density areas</li>
        <li><i class="fa-li fa fa-globe fa-fw"></i>Feedback results</li>
    </ul>
</div>
<div style="float: left;">
    <ul style="list-style: none;">
        <li>tweepy</li>
        <li>gensim</li>
        <li>python-geohash</li>
        <li>scipy/numpy (fast_kde.py)</li>
        <li>numpy</li>
        <li>numpy</li>
        <li>pico+leaflet+D3js</li>
    </ul>
</div>
</div>
</div>
</div><aside class="notes">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Using online Latent Semantic Analysis (LSA) from the gensim Python package, we extract &#39;topics&#39; from tweets in an online training fashion. To maintain real-time relevance, the topic model is continually updated, and depending on parameterization, can &#39;forget&#39; past topics. Based on a set of learned topics, a grid of spatially located tweets for each identified topic is generated using standard numpy and scipy.spatial functionality. Using an efficient streaming algorithm for approximating 2D kernel density estimation (KDE), locations with the highest density of tweets on a particular topic are located.</p>
</div>
</div>
</div>
    </aside></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-twitter-fa-fw-i-twitter-part-is-easy-http-peter-hoffmann-com-2012-simple-twitter-streaming-api-access-with-python-and-oauth-html-"><i class="fa fa-twitter fa-fw"></i> Twitter part is <a href="http://peter-hoffmann.com/2012/simple-twitter-streaming-api-access-with-python-and-oauth.html">easy</a></h1>
<pre><code class="language-python"><span class="keyword">import</span> tweepy
<span class="keyword">import</span> simplejson
<span class="keyword">import</span> sys

consumer_key = <span class="string">''</span>
consumer_secret = <span class="string">''</span>
access_token_key = <span class="string">''</span>
access_token_secret = <span class="string">''</span>

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

BOUNDING_BOX = [xmin, ymin, xmax, ymax]

<span class="class"><span class="keyword">class</span> <span class="title">CustomStreamListener</span><span class="params">(tweepy.StreamListener)</span>:</span>
    <span class="function"><span class="keyword">def</span> <span class="title">on_status</span><span class="params">(self, tweet)</span>:</span>
        print(<span class="string">'Ran on_status'</span>)

    <span class="function"><span class="keyword">def</span> <span class="title">on_error</span><span class="params">(self, status_code)</span>:</span>
        print(<span class="string">'Error: '</span> + repr(status_code))
        <span class="keyword">return</span> <span class="built_in">True</span>  <span class="comment"># Don't die!</span>

    <span class="function"><span class="keyword">def</span> <span class="title">on_data</span><span class="params">(self, data)</span>:</span>
        document = simplejson.loads(data)
        <span class="comment"># Do something awesome with the tweet info...</span>

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=BOUNDING_BOX)
</code></pre>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-quote-right-fa-fw-i-lsa-part-isn-t-easy-http-radimrehurek-com-gensim-tut1-html-corpus-streaming-one-document-at-a-time-"><i class="fa fa-quote-right fa-fw"></i> LSA part <a href="http://radimrehurek.com/gensim/tut1.html#corpus-streaming-one-document-at-a-time">isn&#39;t easy</a></h1>
<ul>
<li>Latent Semantic Analysis<ul>
<li>Analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms</li>
<li>Idea is that words that are close in meaning will occur in similar pieces of text</li>
<li>Latent Semantic Indexing (LSI)</li>
</ul>
</li>
<li>Tokenizing (<a href="https://github.com/myleott/ark-twokenize-py"><code>ark-twokenize-py</code></a>), remove common and unique words (<code>stopwords.py</code>)<ul>
<li><a href="http://www.ark.cs.cmu.edu/TweetNLP/">Twitter NLP</a> and Part-of-Speech Tagging</li>
<li><a href="http://snowball.tartarus.org/">Snowball</a> String Processing Language    </li>
</ul>
</li>
<li><a href="http://en.wikipedia.org/wiki/Bag_of_words">Bag-of-words</a>, and/or <a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf">tf–idf</a> (term frequency–inverse document frequency)</li>
<li>Decay &lt; 1.0 to favor new data trends in input stream</li>
<li>Possibly try Hierarchical Dirichlet Process (because we don&#39;t have to pick # of topics [and gensim has it])</li>
</ul>
<p><br/><br/><br/></p>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-th-fa-fw-i-gridded-topic-counts"><i class="fa fa-th fa-fw"></i> Gridded topic counts</h1>
<ul>
<li>Geohash all coordinates to given scale (optimize for urban environment)<ul>
<li>Convert back to x, y coords (now gridded)</li>
</ul>
</li>
<li>Count unique tweets of given topic<ul>
<li>Normalize counts (by current count and tweet &#39;population&#39;</li>
</ul>
</li>
</ul>
</div>
</div>
</div><div class="fragment">
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-cogs-fa-fw-i-online-kinda-kde"><i class="fa fa-cogs fa-fw"></i> Online (<em>kinda</em>) KDE</h1>
<ul>
<li>Gaussian kernel density estimate<ul>
<li>Convolution of Gaussian kernel with the 2D histogram</li>
</ul>
</li>
<li>Typically several orders of magnitude faster than <code>scipy.stats.kde.gaussian_kde</code> for large (<code>&gt;1e7</code>) numbers of points<ul>
<li>Can handle ~billion points already without too much trouble...</li>
</ul>
</li>
<li>Streaming framework<ul>
<li>Stream 2D histogram binning process</li>
<li>Run convolution on this when needed</li>
</ul>
</li>
<li>Supports weighted KDE<ul>
<li>Take topic component weights when computing KDE</li>
</ul>
</li>
</ul>
</div>
</div>
</div>
    </div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-search-fa-fw-i-identify-events-"><i class="fa fa-search fa-fw"></i> Identify &#39;events&#39;</h1>
<ul>
<li>Locate high-density areas</li>
<li>Right now...<ul>
<li>Let &#39;user&#39; browse current topics &amp; select for viewing</li>
<li>Eventually more automation</li>
</ul>
</li>
<li>Have to get scale right...<ul>
<li>We&#39;re focusing on urban areas (city scale)</li>
</ul>
</li>
</ul>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="-batkid">#batkid</h2>
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/batkid2.png" alt="&#39;#batkid&#39; tweets">
</div>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="concert">concert</h2>
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/concert2.png" alt="&#39;concert&#39; tweets">
</div>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="-drake">#drake</h2>
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/drake2.png" alt="&#39;#drake&#39; tweets">
</div>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="-i-class-fa-fa-globe-fa-fw-i-feedback-results"><i class="fa fa-globe fa-fw"></i> Feedback results</h1>
<ul>
<li><code>Pico</code> - very small web application framework for <code>Python</code><ul>
<li>Bridge between server side <code>Python</code> and client side <code>Javascript</code></li>
</ul>
</li>
<li><code>Pico</code> is a server, a <code>Python</code> libary and a <code>Javascript</code> library!<ul>
<li>Server is a WSGI application</li>
</ul>
</li>
<li><code>Pico</code> allows you to <a href="https://github.com/fergalwalsh/pico/wiki/Streaming-functions">stream</a> data from <code>Python</code> to <code>Javascript</code><ul>
<li>Simply write your function as a <code>Python</code> generator!</li>
</ul>
</li>
</ul>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="write-a-python-module">Write a Python module</h2>
<pre><code class="language-python"><span class="comment"># example.py</span>
<span class="keyword">import</span> pico

<span class="function"><span class="keyword">def</span> <span class="title">hello</span><span class="params">(name=<span class="string">"World"</span>)</span>:</span>
    <span class="keyword">return</span> <span class="string">"Hello "</span> + name
</code></pre>
<h2 id="start-the-server">Start the server</h2>
<pre><code class="language-bash">python -m pico.server
</code></pre>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="call-your-python-functions-from-javascript">Call your Python functions from Javascript</h2>
<pre><code class="language-html"><span class="doctype">&lt;!DOCTYPE HTML&gt;</span>
<span class="tag">&lt;<span class="title">html</span>&gt;</span>
<span class="tag">&lt;<span class="title">head</span>&gt;</span>
  <span class="tag">&lt;<span class="title">title</span>&gt;</span>Pico Example<span class="tag">&lt;/<span class="title">title</span>&gt;</span>
    <span class="tag">&lt;<span class="title">script</span> <span class="attribute">src</span>=<span class="value">"/pico/client.js"</span>&gt;</span><span class="javascript"></span><span class="tag">&lt;/<span class="title">script</span>&gt;</span>
    <span class="tag">&lt;<span class="title">script</span>&gt;</span><span class="javascript">
        pico.load(<span class="string">"example"</span>);
    </span><span class="tag">&lt;/<span class="title">script</span>&gt;</span>
<span class="tag">&lt;/<span class="title">head</span>&gt;</span>
<span class="tag">&lt;<span class="title">body</span>&gt;</span>
  <span class="tag">&lt;<span class="title">p</span> <span class="attribute">id</span>=<span class="value">"message"</span>&gt;</span><span class="tag">&lt;/<span class="title">p</span>&gt;</span>
  <span class="tag">&lt;<span class="title">script</span>&gt;</span><span class="javascript">
  example.hello(<span class="string">"Fergal"</span>, <span class="keyword">function</span>(response){
    document.getElementById(<span class="string">'message'</span>).innerHTML = response;  
  });
  </span><span class="tag">&lt;/<span class="title">script</span>&gt;</span>
<span class="tag">&lt;/<span class="title">body</span>&gt;</span>
<span class="tag">&lt;/<span class="title">html</span>&gt;</span>
</code></pre>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="want-that-to-stream-">Want that to stream?</h2>
<pre><code class="language-python"><span class="keyword">import</span> pico
<span class="keyword">import</span> gevent

<span class="decorator">@pico.stream</span>
<span class="function"><span class="keyword">def</span> <span class="title">stream</span><span class="params">()</span>:</span>
   <span class="keyword">for</span> line <span class="keyword">in</span> open(<span class="string">'long_file.txt'</span>):
      <span class="keyword">yield</span> line
      gevent.sleep(<span class="number">0.1</span>)
</code></pre>
<p>(Plus some other <a href="https://github.com/surfly/gevent"><code>gevent</code></a> magic)</p>
<h2 id="-normal-call-from-javascript">&#39;Normal&#39; call from Javascript</h2>
<pre><code class="language-javascript">example.stream(<span class="keyword">function</span>(line){
   console.log(line)
})
</code></pre>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="where-are-we-at-now-">Where are we at now?</h1>
<ul>
<li>Code and &#39;science&#39; <em>works</em> for the most part<ul>
<li>Nowhere near &#39;production&#39; ready</li>
</ul>
</li>
<li>Web-framework is non-existant (but getting ready)<ul>
<li>My collaborator (<code>pico</code> author) just got a &#39;real-job&#39; and got married</li>
</ul>
</li>
<li>Very happy with how lightweight and &#39;easy&#39; this is to setup<ul>
<li>You can pretty much just drop <code>anaconda</code> or similar on a server and this will work</li>
</ul>
</li>
</ul>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="what-did-we-learn-">What did we learn?</h1>
<ul>
<li>Twitter had the x and y coordinates reversed for a while :-p</li>
<li>People talk about themselves <em>a lot</em>!<ul>
<li>Most tweets <em>at least</em> contain <code>i&#39;m</code>, <code>my</code>, <code>me</code>, etc...</li>
<li>Stopwords and good tokenizing are important!</li>
</ul>
</li>
<li>English language is often ambiguous<ul>
<li>(i.e., this stuff is hard)</li>
</ul>
</li>
<li>Geography <em>is</em> still important<ul>
<li>Many tweets have spatial component and twitter trends <em>do</em> vary geographically</li>
</ul>
</li>
</ul>
</div>
</div>
</div></section><section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="-batkid-versus-everything">#batkid versus everything</h2>
<div style="margin: auto auto; width: 100%; text-align: center;">
<img src="../../images/presentations/all_batkid.png" alt="&#39;#drake&#39; tweets">
</div>
</div>
</div>
</div></section>
    </section><section>
    <section>
    
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="light-weight-real-time-event-detection-with-python">Light-weight real-time event detection with Python</h1>
<p>Carson J. Q. Farmer</p>

<p><i class="fa fa-twitter fa-fw"></i><a href="http://www.twitter.com/carsonfarmer">@carsonfarmer</a><br/>
<i class="fa fa-globe fa-fw"></i><a href="http://www.carsonfarmer.com">carsonfarmer.com</a><br/>
<i class="fa fa-envelope-o fa-fw"></i><a href="mailto:carsonfarmer@gmail.com">carsonfarmer@gmail.com</a><br/>
<i class="fa fa-github-alt fa-fw"></i><a href="https://github.com/cfarmer">github.com/cfarmer</a><br/><br/>
<i class="fa fa-briefcase fa-fw"></i><a href="http://www.hunter.cuny.edu/">Hunter College, City University of New York</a><br/>
<i class="fa fa-map-marker fa-fw"></i><a href="https://www.google.com/maps/place/695+Park+Ave/@40.7687069,-73.9646646,17z/data=!3m1!4b1!4m2!3m1!1s0x89c258ebe705050b:0x22944b98e1be49b7">695 Park Ave, New York, NY, 10065</a></p>
</div>
</div>
</div></section>
    </section>
</div>
</div>

<script src="http://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2/lib/js/head.min.js"></script>

<!-- <script src="reveal.js/js/reveal.js"></script> -->

<script>

// Full list of configuration options available here: https://github.com/hakimel/reveal.js#configuration
Reveal.initialize({
controls: true,
progress: true,
history: true,

theme: Reveal.getQueryHash().theme, // available themes are in /css/theme
transition: Reveal.getQueryHash().transition || 'linear', // default/cube/page/concave/zoom/linear/none

// Optional libraries used to extend on reveal.js
dependencies: [
// { src: "reveal.js/lib/js/classList.js", condition: function() { return !document.body.classList; } },
// { src: "reveal.js/plugin/highlight/highlight.js", async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
// { src: "reveal.js/plugin/notes/notes.js", async: true, condition: function() { return !!document.body.classList; } }
]
});
</script>

<script>
Reveal.addEventListener( 'slidechanged', function( event ) {
  window.scrollTo(0,0);
});
</script>