#read file
import os
import csv

budget_data = os.path. join('PyBank', 'Resources', 'budget_data.csv') 

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    header = next(csvfile)
    
    #find total number of months included in the dataset
    #empty list to hold row 0 (months) count
    rowcount = []

    #read through each row and count the months
    for row in csv_reader:
        rowcount.append(row[0])
        totalnumbermonths = len(rowcount)
    
    print(f" Total number of months {totalnumbermonths}")

    nettotal = []

    for row in csv_reader:
        nettotal.append int(row[1])  
    print(f" Net total is {nettotal}")