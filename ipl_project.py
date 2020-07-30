# Imports

import csv
import json


def total_runs_scored():

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        runs_scored = {}
        next(csv_reader)
        for row in csv_reader:
            team = row[2]
            runs_scored[team] = runs_scored.get(team, 0) + 1

    with open("json_data_files/TotalRunsScored.json", "w") as fp:
        json.dump(runs_scored, fp)


def top_batsman_rcb():

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rcb_batsman = {}
        next(csv_reader)
        for row in csv_reader:
            rcb_team = row[2]
            batsman = row[6]
            batsman_run = int(row[15])
            if rcb_team == 'Royal Challengers Bangalore':
                rcb_batsman[batsman] = rcb_batsman.get(
                    batsman, 0
                    ) + batsman_run

    with open("json_data_files/TopRcbBatsmen.json", "w") as fp:
        json.dump(rcb_batsman, fp)


def foreign_umpire():

    with open('data_source/umpires.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        umpire_country_count = {}
        for row in csv_reader:
            country = row[1]
            if country == 'India':
                continue
            umpire_country_count[country] = umpire_country_count.get(
                country, 0) + 1

    with open("json_data_files/ForeignUmpires.json", "w") as fp:
        json.dump(umpire_country_count, fp)


def matches_team_season():
    with open('data_source/matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        teams_season = {}
        for row in csv_reader:
            season = int(row[1])
            team1 = row[4]
            team2 = row[5]
            teams_season[season] = {}

            for season in teams_season:
                teams_season[season][team1] = teams_season[season].get(
                    team1, 0
                    )+1
                teams_season[season][team2] = teams_season[season].get(
                    team2, 0
                    )+1

    teams_season = dict(sorted(teams_season.items()))
    # print(teams_season)

    with open("json_data_files/TeamsSeasonsGames.json", "w") as fp:
        json.dump(teams_season, fp)


def main():
    total_runs_scored()
    top_batsman_rcb()
    foreign_umpire()
    matches_team_season()


if __name__ == '__main__':
    main()
