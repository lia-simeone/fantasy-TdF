player_picks ={'Lia':['Nairo','Porte','Bardet','Greipel','Valverde'],'John':['Froome','Aru','Sagan','Cavendish','Kreuziger'],'Louis':['Pinot','Contador','Thomas','Kittel','Dumoulin']}

print "Our teams:",player_picks

rank15 = list(range(1,16))

individual_stage_points = dict(zip(rank15,[200,150,120,100,80,60,60,50,40,30,25,20,15,10,5]))

print "Individual stage points:",individual_stage_points

rank20 = list(range(1,21))

daily_gc_points = dict(zip(rank20,[25,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))

print "Daily general classification points:",daily_gc_points

rank30 = list(range(1,31))

final_gc_points = dict(zip(rank30,[500,400,350,300,260,220,200,180,160,140,130,120,110,100,90,80,70,65,60,55,50,45,35,30,25,20,15,10,5]))

print "Final general classification points:",final_gc_points

import csv

reader = csv.reader(open('stage1_results.csv','r'))


