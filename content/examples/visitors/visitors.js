var projection =  geographic()
    .scale(1000);

var path = d3.geo.path()
    .projection(projection)

var svg = d3.select("#chart")
  .append("svg")
    .attr("class", "map")
    .attr("viewBox", "30 0 960 450");

var grids = svg.append("g")
    .attr("id", "grids")
    .attr("class", "Blues");

d3.json("poly.json", function(json) {
  grids.selectAll("path")
      .data(json.features)
    .enter().append("path")
      .attr("d", path)
      .attr("class", quantize)
    .on("mouseover", mouseover_grid)
    .on("mouseout", mouseout_grid)
    .on("mouseleave", mouseout_grid);
});

var names = ['500 and up','100 to 500','50 to 100',
             '20 to 50','10 to 20','1 to 10']

var svg = d3.select("#key")
  .append("svg")
    .attr("class", "chart")
    .attr("width", 100)
    .attr("height", 136);

var blocks = svg.append("g")
  .attr("id", "blocks")
  .attr("class", "Blues")
    .selectAll("rect")
      .data(names)
        .enter().append("rect")
    .attr("width", 20)
    .attr("x", 0)
    .attr("y", function(d) {return(names.indexOf(d) * 22)})
    .attr("height", 20)
    .attr("class", function(d) {return("q" + (5-names.indexOf(d)) + "-6")})
    .on("mouseover", mouseover_block)
    .on("mouseout", mouseout_block);
    
var labels = svg.append("g")
  .attr("id", "labels")
    .selectAll("text")
      .data(names)
        .enter().append("text")
    .attr("x", 24)
    .text(function(d) {return(d)})
    .attr("y", function(d) {return(names.indexOf(d) * 22 + 15)});

function quantize(d) {
  function sortit(x, y) {
    return (x-y)
  }
  var breaks = [11, 21, 51, 101, 501, 2001, d.properties.count].sort(sortit);
  var t = "q" + breaks.indexOf(d.properties.count) + "-6";
  return t;
};

function get_name(d) {
  var t = d.properties;
  return (t.city ? t.city : "Unknown city");
};

function get_count(d) {
  var t = d.properties;
  return "with " + t.count + " unique visitors";
}

function mouseover_grid(d) {
  d3.select(this)
    .transition()
      .duration(50)
      .attr("transform", function(d) {
            var centroid = path.centroid(d),
            x = centroid[0],
            y = centroid[1];
            return "translate(" + x + "," + y + ")"
            + "scale(3, 3)"
            + "translate(" + -x + "," + -y + ")";})
  // append this to its parent (which will move it to the 'top')
  this.parentNode.appendChild(this)
  d3.select(".place-name")
    .text(get_name(d))
  d3.select(".place-count")
    .text(get_count(d))
};

function mouseout_grid(d) {
  d3.select(this)
    .transition()
      .duration(50)
      .attr("transform", "scale(1,1)");
  d3.select(".place-name")
    .text("")
  d3.select(".place-count")
    .text("")
};

function mouseover_block(d, i) {
  d3.select(this)
    .transition()
      .duration(10)
      .attr("stroke-width", 3);

  var cls = this.attributes.class.value
  d3.selectAll("#grids").selectAll('path')
    .filter(function(x) {return(quantize(x) == cls)})
    .transition()
      .duration(50)
      .attr("transform", function(b) {
            var centroid = path.centroid(b),
            x = centroid[0],
            y = centroid[1];
            return "translate(" + x + "," + y + ")"
            + "scale(3, 3)"
            + "translate(" + -x + "," + -y + ")";})
      .each(function(d, i) {this.parentNode.appendChild(this)});
};

function mouseout_block(d) {
  d3.select(this)
    .transition()
      .duration(10)
      .attr("stroke-width", 0);

  var cls = this.attributes.class.value
  d3.selectAll("#grids").selectAll('path')
    .filter(function(x) {return(quantize(x) == cls)})
    .transition()
      .duration(50)
      .attr("transform", "scale(1,1)");
};
