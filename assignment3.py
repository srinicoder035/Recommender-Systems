import csv
from operator import itemgetter
import itertools
filename = "movie_metadata.csv"

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("Total no of rows %d"%(csvreader.line_num))
actor = input("Enter the actor\n")
data = []
query = 'actor_1_name == "' + actor +'" or actor_2_name == "' + actor + '" or actor_3_name == "' + actor + '"'

for i in range (len(rows)):
    for j in range(len(fields)):
        exec(fields[j] + ' = ' + '"' + rows[i][j] + '"')

    if(eval(query)):
        fl = 0
        for j in range(len(data)):
            if data[j] == rows[i]:
                fl = 1
                break
        if fl == 0:
            data.append(rows[i])
        
for i in range(len(data)):
    data[i][25] = float(data[i][25])
    data[i][27] = float(data[i][27])
    data[i].append(data[i][25] + data[i][27])

sort_data = sorted(data,key = itemgetter(28),reverse=True)


print("\nThe top 5 movies of %s are"%(actor))
for i in range(0,5):
    print(sort_data[i][11])