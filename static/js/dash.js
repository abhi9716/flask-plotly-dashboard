


fill = d3.scale.category20();
layout = d3.layout.cloud()
.size([500, 300])
.words(word_freqs)
.padding(5)
.rotate(0)
.font("Impact")
.fontSize(function(d) {
  return (d.size/max_freq)*100;
})
.on("end", draw);
layout.start();
function draw(words) {
  document.getElementById("bargraph1").innerHTML = ""
  d3.select("#bargraph1").append("svg")
  .attr("width", layout.size()[0])
  .attr("height", layout.size()[1])
  .attr("style", "display: block; margin-left: auto; margin-right: auto; background: #194661; text-align: center; border-radius: 7px 7px 7px 7px; -moz-border-radius: 7px 7px 7px 7px; -webkit-border-radius: 7px 7px 7px 7px; border: 0px solid #f0f0f5;")
  .append("g")
  .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
  .selectAll("text")
  .data(words)
  .enter().append("text")
  .style("font-size", function(d) { return d.size + "px"; })
  .style("font-family", "Impact")
  .style("fill", function(d, i) { return fill(i); })
  .attr("text-anchor", "middle")
  .attr("transform", function(d) {
    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
  })
  .text(function(d) { return d.text; });
}


var feat=[]
var prod=[]

Plotly.plot('bargraph',graphs,{});

async function myFunction() {
  feat = document.getElementById("select1");
  prod = document.getElementById("select");
  console.log(feat.value)
  console.log(prod.value)
  var entry = {
    feat : feat.value,
    prod : prod.value
  };
  console.log(entry)
  const response = await fetch(`${window.origin}/bar`,{
    method: "POST",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })

  .then(async function(response) {
    if (response.status !== 200) {
      return console.log('Looks like there was a problem. Status code:');  
    }

     


      // console.log(data)
      const resData = await response.json()
      data=resData
      Plotly.newPlot('bargraph', JSON.parse(data["plot"]),{});
      console.log(data["plot"])

      var word_freqs = data["word_freqs"];
      max_freq = data["max_freq"];
      fill = d3.scale.category20();
      layout = d3.layout.cloud()
      .size([500, 300])
      .words(word_freqs)
      .padding(5)
      .rotate(0)
      .font("Impact")
      .fontSize(function(d) {
        return (d.size/max_freq)*100;
      })
      .on("end", draw);

      layout.start();

      function draw(words) {
        document.getElementById("bargraph1").innerHTML = ""

        d3.select("#bargraph1").append("svg")
        .attr("width", layout.size()[0])
        .attr("height", layout.size()[1])
        .attr("style", "display: block; margin-left: auto; margin-right: auto; background: #194661; text-align: center; border-radius: 37px 37px 37px 37px; -moz-border-radius: 37px 37px 37px 37px; -webkit-border-radius: 37px 37px 37px 37px; border: 0px solid #000000;")
        .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
      }
    })

}





   // console.log("sdjhvbjdvhncdfjkcmdfkcvvcdfcvhjbh")