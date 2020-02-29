// this function is run when the page loads
function main() {
    console.log("Beginning main()");
    console.log(d3.json);
    d3.json("/api/weeklydata").then(data =>console.log(data));
}





main(); // initialize the page