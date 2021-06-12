var url = "http://127.0.0.1:5000/api";

// Fetch the JSON data and console log it
d3.json(url).then(function(response) {
    var y0 = []
    var x0 = []
    for (var i = 0; i < response.length; i++) {

        var location = response[i];
        var minSalary = location['Min Salary Estimate'].substring(1);
        var maxSalary = location['Max Salary Estimate'].substring(1)
        var industry = location['Industry']
        y0.push(minSalary)
        y0.push(maxSalary)
        x0.push(industry)
    }   var trace1 = {
            y: y0,
            x: x0,
            name: "Jobs",
            marker: {color: '#FF4136'},
            type: 'box'
        };
        var layout = {
            title: 'Box Plot of Data Salaries by Industry',
            yaxis: {
                title: 'Salaries in Dollars',
                zeroline: false
              }
        };

        var data = [trace1]
        Plotly.newPlot('plot', data, layout);
    });
    