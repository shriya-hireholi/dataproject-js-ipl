# Imports

import csv
import json
from ipl_teams import teams as team_list


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
                    batsman, batsman_run
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
        matches = []
        for i in csv_reader:
            matches.append(i)

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        deliveries = []
        for i in csv_reader:
            deliveries.append(i)

    def merge(lst1, lst2):
        return [a + [b[1]] for (a, b) in zip(lst1, lst2)]

    mergedlst = merge(deliveries, matches)

    i = 0
    s = {}

    for r in mergedlst:
        if i == 0:
            i += 1
        else:
            if r[21] not in s:
                if r[21] not in s:
                    s[r[21]] = {}

    for i in team_list:
        for key in sorted(s):
            s[key][i] = 0

    for x in matches:
        if x[1] in s and x[4] in s[x[1]] and x[5] in s[x[1]]:
            s[x[1]][x[4]] += 1
            s[x[1]][x[5]] += 1

    s = dict(sorted(s.items()))
    # print(s)

    with open("json_data_files/TeamsSeasonsGames.json", "w") as fp:
        json.dump(s, fp)


def main():
    total_runs_scored()
    top_batsman_rcb()
    foreign_umpire()
    matches_team_season()


if __name__ == '__main__':
    main()
