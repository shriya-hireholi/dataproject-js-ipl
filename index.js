function total_runs_team(){
    const runsScored= [];
    fetch("json_data_files/TotalRunsScored.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let team in data){
            runsScored.push([team,data[team]]);
            Highcharts.chart("total-runs-scored",{
                chart: {
                    type: "column"
                },
                title: {
                    text: "Total Runs scored"
                },
                xAxis: {
                    type: "category",
                    title: {
                        text: "Teams Played"
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: "No. of Games Played"
                    }
                },
                series: [
                    {
                        colorByPoint: true,
                        name: "teams",
                        data: runsScored
                    }
                ]
            });
        }
    });
}


function top_rcb_batsmen(){
    const topBatsmen= [];
    fetch("json_data_files/TopRcbBatsmen.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let batsmen in data){
            topBatsmen.push([batsmen,data[batsmen]]);
            Highcharts.chart("top-rcb-batsmen",{
                chart: {
                    type: "bar"
                },
                title: {
                    text: "Top Batsmen"
                },
                xAxis: {
                    type: "category",
                    title: {
                        text: "Batsmen"
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: "Runs Scored"
                    }
                },
                series: [
                    {
                        name: "batsmen",
                        data: topBatsmen
                    }
                ]
            });
        }
    });
}

function foreign_umpires(){
    const umpires= [];
    fetch("json_data_files/ForeignUmpires.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let ump in data){
            umpires.push([ump,data[ump]]);
            Highcharts.chart("foreign-umpires",{
                chart: {
                    type: "column"
                },
                title: {
                    text: "Foreign Umpires"
                },
                xAxis: {
                    type: "category",
                    title: {
                        text: "Umpires"
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: "Countries"
                    }
                },
                series: [
                    {
                        colorByPoint: true,
                        name: "No. of umpires",
                        data: umpires
                    }
                ]
            });
        }
    });
}

function teams_seasons_games(){
    
    const processed_json = [];
    fetch("json_data_files/TeamsSeasonsGames.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let year in data){
            var teamSeason= {};
            teamSeason["name"] = year;
            teamSeason["data"] = Object.entries(data[year]);
            processed_json.push(teamSeason);
        }
        Highcharts.chart("team-games-season",{
            chart: {
                type: "column"
            },
            title: {
                text: "Games played by Teams by Season"
            },
            xAxis: {
                type: "category",
                title: {
                    text: "Teams"
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: "Number of Games Played"
                }
            },
            plotOptions: {
                column: {
                    stacking: 'number'
                }
            },
            series: processed_json
        });   
    });
}

total_runs_team();
top_rcb_batsmen();
foreign_umpires();
teams_seasons_games();