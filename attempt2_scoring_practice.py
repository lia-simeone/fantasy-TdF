# import packages
from __future__ import division, print_function
import sys
import pandas as pd

def main():
    # assign riders to each player based on the draft
    rider_picks = {'Quintana': 'Lia', 'Porte':'Lia', 'Bardet':'Lia', 'Greipel':'Lia', 'Valverde':'Lia',
                   'Froome': 'John', 'Aru': 'John', 'Sagan': 'John', 'Cavendish': 'John', 'Kreuziger': 'John',
                   'Pinot': 'Louis', 'Contador': 'Louis', 'Thomas': 'Louis', 'Kittel': 'Louis', 'Dumoulin': 'Louis'}

    # store the amount of points we'll give for finishing
    stage_points = dict(zip(list(range(1,16)),
                            [200, 150, 120, 100, 80, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5]))
    daily_gc_points = dict(zip(list(range(1,21)),
                               [25, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    final_gc_points = dict(zip(list(range(1,31)),
                               [500, 400, 350, 300, 260, 220, 200, 180, 160, 140, 130, 120, 110, 100,
                                90, 80, 70, 65, 60, 55, 50, 45, 35, 30, 25, 20, 15, 10, 5]))

    # create a placeholder for the overall standings
    fantasy_standings = {'Lia': 0, 'John': 0, 'Louis' :0}

    # read in the results
    stage_df = pd.read_csv('stage_standings.csv', index_col = 'rank')
    daily_gc_df = pd.read_csv('daily_gc_standings.csv', index_col = 'rank')

    # figure out which of the top ranked riders are actually on our fantasy teams
    def get_relevant_riders(standings_series):
        # turn each stage result into a dictionary
        stage_results = standings_series.to_dict()
        # swap the dictionary so the rider is the key and his rank the value
        stage_results_transposed = {val: key for (key, val) in stage_results.items()}

        # grab only the riders that are on our teams
        relevant_riders = {rider: rank for (rider, rank) in stage_results_transposed.items() if rider in rider_picks.keys()}
        return relevant_riders


    # run the scoring up to the stage specified in the command line
    for stage in range(1, int(sys.argv[1]) + 1):

        # create a placeholder for the stage points
        stage_standings = {'Lia': 0, 'John': 0, 'Louis': 0}

        # increase the stage scores for each player based on where their riders finished in the stage
        for rider, rank in get_relevant_riders(stage_df[str(stage)]).items():
            stage_standings[rider_picks[rider]] += stage_points[rank]

        # increase the stage scores for each player based on where their riders finished in the overall GC
        for rider, rank in get_relevant_riders(daily_gc_df[str(stage)]).items():
            stage_standings[rider_picks[rider]] += daily_gc_points[rank]

        # increase the overall scores based on how well our riders did
        for player, points in fantasy_standings.items():
            fantasy_standings[player] += stage_standings[player]

        # print the results after each stage
        print("")
        print("Stage {0} results: {1}".format(stage, stage_standings))
        print("Overall results after stage {0}: ".format(stage, fantasy_standings))

if __name__ == "__main__":
    main()
