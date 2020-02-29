// this function is run when the page loads
function main() {
    console.log("Beginning main()");
    weeklyChart();
    salaryTable();
}

// this function plots a chart of weekly data (called from main, above)
function weeklyChart() {
    d3.json("/api/weeklydata").then(rows => {
        console.log(rows);
        let data = sqlToTrace(rows, "day", "value");
        let options = { margin: { t: 0 } };
        Plotly.newPlot("chartDiv", [data], options); // remember - plotly wants an array of data (one per trace)
    });
}

// this function plots a table of 
function salaryTable() {
    d3.json("/api/salarydata").then(rows => {
        let tableData = [{
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
                values: sqlToTable(rows),
                align: "center",
                line: { color: "black", width: 1 },
                font: { family: "Arial", size: 11, color: ["black"] }
            }
        }];

        Plotly.newPlot('tableDiv', tableData);
    });
}
function sqlToTrace(rows, xname, yname) {
    let x = [];
    let y = [];
    for (row of rows) {
        x.push(row[xname]);
        y.push(row[yname]);
    }
    return { x, y };
}
function sqlToTable(rows) {
    let header = [];
    let body = [];
    for (heading in rows[0]) {// getting the object keys
        header.push(heading);
    }
    body.push(header);
    for (row of rows) {
        body.push(Object.values(row))
    }
    return body;
}



main(); // initialize the page