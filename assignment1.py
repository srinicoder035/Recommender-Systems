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
movie = input("Enter the movie\n")
data = []
query = 'movie_title == "' + movie +'"'

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

search = data[0][16]
search = search.split("|")
print("The keywords are as follows ")
print(search)

print("The movies in the above keywords are  ")
count = 0
for i in range (len(rows)):
    find = rows[i][16].split("|")
    for x in find:
        if x in search:
            count+=1
            print(rows[i][11])
            break

print("Total number of matches is : %d"%(count))
