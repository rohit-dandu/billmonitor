var width = 450
    height = 450

var radius = Math.min(width, height) / 2 - 30

var svg = d3.select("#pie")
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var color = d3.scaleOrdinal()
  .domain(data).range(d3.schemeSet2);

var pie = d3.pie().value(function(d) {return d.value; })
var final_data = pie(d3.entries(data))

var arcGenerator = d3.arc()
  .innerRadius(0)
  .outerRadius(radius)

svg
  .selectAll('mySlices').data(final_data).enter().append('path')
  .attr('d', arcGenerator).attr('fill', function(d){ return(color(d.data.key)) }).attr("stroke", "black").style("stroke-width", "2px").style("opacity", 0.7)

svg
  .selectAll('mySlices').data(final_data).enter().append('text')
  .text(function(d){ return d.data.key})
  .attr("transform", function(d) { return "translate(" + arcGenerator.centroid(d) + ")";  })
  .style("text-anchor", "middle").style("font-size", 17)