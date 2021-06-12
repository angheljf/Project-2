var url = "http://127.0.0.1:5000/api";

// Fetch the JSON data and console log it
d3.json(url).then(function(response) {
    var y0 = []
    var x0 = []
    for (var i = 0; i < response.length; i++) {

        var location = response[i]
        var rating = location['Rating']
        var avgSalary = location['Avg Salary Estimate'].substring(1)
        var industry = location['Industry']
        y0.push(rating)
        // y0.push(maxSalary)
        x0.push(industry)
    }   var trace1 = {
            y: y0,
            x: x0,
            name: "Salary",
            marker: {color: '#58FA58'},
            type: 'box'
        };
        var layout = {
            title: 'Box Plot of Ratings by Industry',
            yaxis: {
                title: 'Ratings',
                zeroline: false
              }
        };

        var data = [trace1]
        Plotly.newPlot('plot', data, layout);
    });
    