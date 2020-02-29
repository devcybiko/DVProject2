// this function is run when the page loads
function main() {
    console.log("Beginning main()");
    weeklyChart();
    salaryTable();
}

function weeklyChart() {
    d3.json("/api/weeklydata").then(rows => {
        console.log(rows);
        let data = sqlToPlotly(rows, "day", "value");
        let options = { margin: { t: 0 } };
        let chartDiv = document.getElementById('chart');
        Plotly.newPlot(chartDiv, [data], options); // remember - plotly wants an array of data (one per trace)
    });
}

function salaryTable() {

    var data = [{
        type: 'table',
        header: {
            values: [["<b>EXPENSES</b>"], ["<b>Q1</b>"],
            ["<b>Q2</b>"], ["<b>Q3</b>"], ["<b>Q4</b>"]],
            align: "center",
            line: { width: 1, color: 'black' },
            fill: { color: "grey" },
            font: { family: "Arial", size: 12, color: "white" }
        },
        cells: {
            values: values,
            align: "center",
            line: { color: "black", width: 1 },
            font: { family: "Arial", size: 11, color: ["black"] }
        }
    }]

    Plotly.newPlot('table', data);
}

function sqlToPlotly(rows, xname, yname) {
    let x = [];
    let y = [];
    for (row of rows) {
        x.push(row[xname]);
        y.push(row[yname]);
    }
    return { x, y };
}



main(); // initialize the page