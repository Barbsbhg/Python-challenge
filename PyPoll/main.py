#read file
import os
import csv

election_data = os.path. join('..','PyPoll', 'Resources', 'election_data.csv') 

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

     # skip the header row
    header = next(csvfile)

    candidaterow = {}
    totalvotes = 0
    for row in csv_reader:
        totalvotes += 1
        candidate = row[2]
        if candidate in candidaterow:
            candidaterow[candidate] += 1
        else:
            candidaterow[candidate] = 1

print(f"Total Votes {totalvotes}")


     

