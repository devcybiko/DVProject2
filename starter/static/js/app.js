// this function is run when the page loads
function main() {
    console.log("Beginning main()");
    console.log(d3.json);
    d3.json("/api/weeklydata").then(rows => {
        console.log(rows);
        let data = sqlToPlotly(rows, "day", "value");
        let options = {margin: {t: 0}};
        let chartDiv = document.getElementById('chart');
        Plotly.newPlot(chartDiv, data, options);
    });
}

function sqlToPlotly(rows, xname, yname) {
    let x = [];
    let y = [];
    for(row of data) {
        x.push(row[xname]);
        y.push(row[yname]);
    }
    return {x, y};
}



main(); // initialize the page