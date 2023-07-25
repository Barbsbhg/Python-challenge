import os
import csv


bankcsv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(bankcsv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    header = next(csvfile)
    print(f"header: {header}")
    
    rowcount = []

    for row in csv_reader:
        rowcount.append(row[0])
        totalnumbermonths = len(rowcount)
    
    print(str(totalnumbermonths))
