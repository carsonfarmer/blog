Title: After the Irish famine
Date: 2014-03-27 12:00
Author: cfarmer
Slug: maps/irish_famine
Icon: fa-map-marker
Status: hidden
Template: full_page

<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/topojson.v1.min.js"></script>
<script src="../../libs/cartogram/colorbrewer.js"></script>
<script src="../../libs/cartogram/cartogram.js"></script>
<link rel="stylesheet" href="../../libs/cartogram/style.css">
<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
<script src="http://code.jquery.com/ui/1.10.4/jquery-ui.js"></script>

<img id="bg" src="{filename}/images/famine/bg-1024.png" style="position: fixed; top: 0; left: 0;">
<div id="map">
<div class="bold_title">
    <h2><i class="fa fa-map-marker"></i> After the Irish famine</h2>
</div>
  <div id="map-container">
    <div class="floater shadow">
      <label>Scale by population from</label>&nbsp;<label id="yearlabel" name="yearlabel">1841</label>
      <div class="slider" id="year" name="year"></div>
      <span id="status"></span><br/>
        <div class="share-list">
            <a href="http://twitter.com/share?url=http://www.carsonfarmer.com/maps/irish_famine&text=After the Irish Famine&hashtags=famine,irish,cartogram,d3js&via=CarsonFarmer"
              onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,height=600,width=600');return false;"
              class="label label-primary">
              <i class="fa fa-twitter-square fa-2x"></i>
            </a>
            <a href="https://plus.google.com/share?url=http://www.carsonfarmer.com/maps/irish_famine" 
              onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,height=600,width=600');return false;"
              class="label label-primary">
              <i class="fa fa-google-plus-square fa-2x"></i>
            </a>
            <a href="http://www.linkedin.com/shareArticle?mini=true&url=http://www.carsonfarmer.com/maps/irish_famine&title=After the Irish Famine&source=CarsonFarmer"
              onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,height=600,width=600');return false;"
              class="label label-primary">
              <i class="fa fa-linkedin-square fa-2x"></i>
            </a>
            <a href="http://www.tumblr.com/share/link?url=http://www.carsonfarmer.com/maps/irish_famine&name=After the Irish Famine"
              onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,height=600,width=600');return false;"
              class="label label-primary">
              <i class="fa fa-tumblr-square fa-2x"></i>
            </a>
            <a href="http://www.facebook.com/sharer.php?s=100&p[url]=http://www.carsonfarmer.com/maps/irish_famine&p[title]=After the Irish Famine"
              onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,height=600,width=600');return false;"
              class="label label-primary">
              <i class="fa fa-facebook-square fa-2x"></i>
            </a>
            <a href="#" class="modal-toggle label label-primary" data-toggle="modal" data-target="#myModal"><i class="fa fa-info-circle fa-2x"></i></a>
        </div>
    </div>
    <svg id="d3map"></svg>
  </div>
</div> 

<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h2 class="modal-title" id="myModalLabel">About</h2>
      </div>
      <div class="modal-body">
        <p>This is a simple visualization of population change in Ireland 
            during the 
            <a href="http://en.wikipedia.org/wiki/Great_Famine_(Ireland)">Great Famine</a> era. 
            It uses continuous area cartograms and population estimates from 
            1841 to 2001 to demonstrate change. The cool thing about this visualization is how 
            dramatically it emphasizes population loss from 1841 to 1851 
            (and beyond), and how, even in modern Ireland, many counties 
            remain well below their pre-famine population levels. As a 
            whole, the population of Ireland remains less than 70% of its 
            pre-famine levels!</p>
            <p>A popover gives you additional information on mouse over. This 
            includes county name, total population for the give year, and
            a nice little <a href="http://en.wikipedia.org/wiki/Sparkline">sparkline</a>
            showing population change over time (with 
            the current year highlighted for reference). This gives a nice quick
            feel for the population change over time, and was pretty easy to do 
            using D3js and Twitter Bootstrap.</p>
            <p>This visualization uses <a href="http://d3js.org">D3js</a>, 
            <a href="http://colorbrewer2.org">colorbrewer</a>, 
            <a href="http://getbootstrap.com/">Twitter's Bootstrap</a>, 
            <a href="http://jquery.com/">jQuery</a>, and some helpful examples from 
            <a href="http://www.tnoda.com/blog/2013-12-19">here</a>,
            <a href="http://benjchristensen.com/2011/08/08/simple-sparkline-using-svg-path-and-d3-js/">here</a>, and
            <a href="http://jsfiddle.net/eQmYX/77/">here</a> (among others). There is also a
        <a class="hashish" href="?segmentized">segmentized topology</a>,
        which distorts the shapes a bit more fluidly than the
        <a class="hashish" href="?">original</a>.</p>
        <p>Code based heavily on the 
  <a href="https://github.com/shawnbot/d3-cartogram">d3-cartogram</a>
  example by <a href="http://stamen.com/studio/shawn">Shawn Allen</a> at 
  <a href="http://stamen.com">Stamen</a>.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<script>

  var percent = (function() {
        var fmt = d3.format(".2f");
        return function(n) { return fmt(n) + "%"; };
      })(),
      years = d3.range(1841,1912, 10).concat([1926, 1936]).concat(d3.range(1951, 2011, 10)),
      year = years[0],
      colors = colorbrewer.RdYlBu[3]
        .reverse()
        .map(function(rgb) { return d3.hsl(rgb); });

  $('#year').slider({min:0, max:15, step:1, value:0})
  .on('slide', function(e, ui) {
      year = years[parseInt(ui.value)];
      d3.select("#yearlabel").text(" "+year);
  }).on('slidechange', function(e, ui) {
      year = years[parseInt(ui.value)];
      location.hash = "#" + year;
  });

  var body = d3.select("body"),
      stat = d3.select("#status");

  var map = d3.select("#d3map"),
      layer = map.append("g")
        .attr("id", "layer")
        .attr("transform", "translate(-180, 0)"),
      counties = layer.append("g")
        .attr("id", "counties")
        .selectAll("path");

  // map.call(zoom);

  var proj = d3.geo.albers()
      .scale(7307.831779290534)
      .center([-0.6, 38.7])
      .translate([978.8244047152583, 2145.7113504855133])
      .rotate([0, 0, 0]);

  var topology,
      geometries,
      rawData,
      dataById = {},
      carto = d3.cartogram()
        .projection(proj)
        .properties(function(d) {
          return dataById[d.id];
        })
        .value(function(d) {
          return +d.properties[field];
        });

  window.onhashchange = function() {
    parseHash();
  };

  var segmentized = location.search === "?segmentized"
  var url = "../../uploads/data/" + (segmentized ? "irish-counties-segmentized.topojson" : "irish-counties.topojson"),
      totalValue = 0;
  d3.json(url, function(topo) {
    topology = topo;
    geometries = topology.objects.counties.geometries;
    d3.csv("../../uploads/data/pop.csv", function(data) {
      rawData = data;
      dataById = d3.nest()
        .key(function(d) { return d.county; })
        .rollup(function(d) { return d[0]; })
        .map(data);
      init();
    });
  });

  function init() {
    var features = carto.features(topology, geometries),
        path = d3.geo.path()
          .projection(proj);
    var key = "pop" + years[0];

    counties = counties.data(features)
      .enter()
      .append("path")
        .attr("class", "county")
        .attr("id", function(d) {
          return d.id;
        })
        .attr("fill", "#fafafa")
        .attr("title", function(d) {return "County "+d.id;})
        .attr("d", path);
        
        var value = function(d) {
              return +d.properties[key];
            },
          values = counties.data()
            .map(value)
            .filter(function(n) {
              return !isNaN(n);
            })
            .sort(d3.ascending),
          lo = values[0],
          hi = values[values.length - 1];
          
          var scale = d3.scale.linear()
            .domain([lo, hi])
            .range([1, 1000]);
            
        totalValue = d3.sum(values)//, scale);
    
    function sparkline() {
        var svg = d3.select(document.createElement("svg"))
          .attr("height", "40px")
          .attr("width", "110px");
        g = svg.append("g")
            .attr('transform', 'translate(5, 5)'),
            data = dataById[this.id];
            var array = $.map(data, function(value, index) {
                return +value;
            });
        var format = d3.format(','),
            array = array.slice(1, array.length),
            yearIndex = years.indexOf(year),
            currentPop = array[yearIndex],
            minmax = d3.extent(array);
        var x = d3.scale.linear().domain([0, 16]).range([0, 100]), 
            y = d3.scale.linear().domain(minmax).range([30, 0]), 
            line = d3.svg.line()
              .x(function(d, i) { return x(i); })
              .y(function(d)    { return y(d); });
        g.append("path")
          .attr("d", line(array))
          .attr("class", "sparkline");
        g.append('circle')
          .attr('class', 'sparkcircle')
          .attr('cx', x(yearIndex))
          .attr('cy', y(currentPop))
          .attr('r', 3);
        var percent = Math.round(currentPop / array[0] * 100)
        
        return "Year: " + year
            + "<br/>"
            + "Population: " + format(currentPop)
            +"<br/>"
            +"<svg height='40px' width='100%'>"
            +svg.node().innerHTML
            +"</svg><br/>"
            +(yearIndex > 0 ? (percent >= 100 ? "Up "+(percent-100): "Down "+(100-percent))+"% since 1941": "")
            
    }
    
    $("path").popover({
        'container': 'body',
        'html': true,
        'content': sparkline,
        'placement': "auto",
        'trigger': "hover"
    });

    parseHash();
  }

  function reset() {
    stat.text("");
    body.classed("updating", false);

    var features = carto.features(topology, geometries),
        path = d3.geo.path()
          .projection(proj);

    counties.data(features)
      .transition()
        .duration(750)
        .ease("linear")
        .attr("fill", "#fafafa")
        .attr("d", path);
  }

  function update() {
    var start = Date.now();
    body.classed("updating", true);

    var key = "pop" + year,
        value = function(d) {
          return +d.properties[key];
        },
        values = counties.data()
          .map(value)
          .filter(function(n) {
            return !isNaN(n);
          })
          .sort(d3.ascending),
        lo = values[0],
        hi = values[values.length - 1];

    var color = d3.scale.linear()
      .range(colors)
      .domain(lo < 0
        ? [lo, 0, hi]
        : [lo, d3.mean(values), hi]);

    // normalize the scale to positive numbers
    var scale = d3.scale.linear()
      .domain([lo, hi])
      .range([1, 1000]);

    // tell the cartogram to use the scaled values
    carto.value(function(d) {
      //return scale(value(d));
      return value(d);
    });

    // generate the new features, pre-projected
    var features = carto(topology, geometries, totalValue).features;

    // update the data
    counties.data(features);

    // transition shapes
    counties.transition()
      .duration(750)
      .ease("linear")
      .attr("fill", function(d) {
        return color(value(d));
      })
      .attr("d", carto.path)

    var delta = (Date.now() - start) / 1000;
    stat.text(["calculated in", delta.toFixed(1), "seconds"].join(" "));
    body.classed("updating", false);
    
  }

  var deferredUpdate = (function() {
    var timeout;
    return function() {
      var args = arguments;
      clearTimeout(timeout);
      stat.text("calculating...");
      return timeout = setTimeout(function() {
        update.apply(null, arguments);
      }, 10);
    };
  })();

  var hashish = d3.selectAll("a.hashish")
    .datum(function() {
      return this.href;
    });

  function parseHash() {
    var parts = location.hash.substr(1).split("/"),
        desiredYear = parseInt(parts[0]);
    year = (years.indexOf(desiredYear) > -1) ? desiredYear : years[0];

      deferredUpdate();
      location.replace("#" + year);

      hashish.attr("href", function(href) {
        return href + location.hash;
      });
      
      // If not already, match slider to hash year
      $('#year').slider("value", years.indexOf(desiredYear))
      d3.select("#yearlabel").text(" "+year);
    }

</script>
<script src="../../theme/js/tools.js"></script>
<script>
size_background("../../images/famine/")
</script>