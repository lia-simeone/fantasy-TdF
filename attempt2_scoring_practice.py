# import packages
import sys
import pandas as pd

# align riders to teams based on the draft
rider_picks = {'Quintana':'Lia','Porte':'Lia','Bardet':'Lia','Greipel':'Lia','Valverde':'Lia','Froome':'John','Aru':'John','Sagan':'John','Cavendish':'John','Kreuziger':'John','Pinot':'Louis','Contador':'Louis','Thomas':'Louis','Kittel':'Louis','Dumoulin':'Louis'}

# create the points given based on finishing ranks
stage_points = dict(zip(list(range(1,16)),[200,150,120,100,80,70,60,50,40,30,25,20,15,10,5]))
daily_gc_points = dict(zip(list(range(1,21)),[25,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
final_gc_points = dict(zip(list(range(1,31)),[500,400,350,300,260,220,200,180,160,140,130,120,110,100,90,80,70,65,60,55,50,45,35,30,25,20,15,10,5]))

# create a placeholder for the overall standings
fantasy_standings = {'Lia':0,'John':0,'Louis':0}

# read in the results
stage_df = pd.read_csv('stage_standings.csv',index_col='rank')
daily_gc_df = pd.read_csv('daily_gc_standings.csv',index_col='rank')

def add_points(standings):



# run the scoring up to the stage specific in the command line
for stage in range(1,int(sys.argv[1])+1):

    # create a placeholder for the stage points
    stage_standings = {'Lia':0,'John':0,'Louis':0}


    # turn each stage result into a series
    stage_results = stage_df[str(stage)].to_dict()
    # make the rider the key and his rank the value
    stage_results_transposed = {val:key for (key, val) in stage_results.items()}

    # grab only the riders that are on our teams
    relevant_riders = {rider:rank for (rider,rank) in stage_results_transposed.items() if rider in rider_picks.keys()}

    # increase the stage scores based on the stage finishings
    for rider,rank in relevant_riders.items():
        stage_standings[rider_picks[rider]] += stage_points[rank]



    # turn each GC result into a series
    daily_gc_results = daily_gc_df[str(stage)].to_dict()
    # make the rider the key and his rank the value
    daily_gc_results_transposed = {val:key for (key, val) in daily_gc_results.items()}

    # grab only the riders that are on our teams
    relevant_riders = {rider:rank for (rider,rank) in daily_gc_results_transposed.items() if rider in rider_picks.keys()}

    # increase our score based on how well our riders did
    for rider,rank in relevant_riders.items():
        stage_standings[rider_picks[rider]] += daily_gc_points[rank]




    # increase the overall scores based on how well our riders did
    for player,points in fantasy_standings.items():
        fantasy_standings[player] += stage_standings[player]


    # print the results after each stage
    print ""
    print "Stage",stage,"results:",stage_standings
    print "Overall results after stage",stage,":",fantasy_standings
