#read file
import os
import csv

budget_data = os.path. join('..','PyBank', 'Resources', 'budget_data.csv') 

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    header = next(csvfile)
    
    #find total number of months included in the dataset
    #empty list to hold row 0 (months) count
    rowcount = []
    nettotal = []
    changedrevenue = []
    previous = 0
    #read through each row and count the months and sum of profit losses
    for rows in csv_reader:
        rowcount.append(rows[0])
        nettotal.append(int(rows[1]))
        totalnumbermonths = len(rowcount)
    #changes in "Profit/Losses"
        changed = int(rows[1]) - previous
        previous = int(rows [1]) 
        changedrevenue.append(changed)
    changedrevenue.pop(0)
    average = sum(changedrevenue)/(totalnumbermonths-1) 

    print(f" Total number of months {totalnumbermonths}")
    
    nettotal = int(sum(nettotal))
    print(f"The net total amount of Profit/Losses ${nettotal}")
    print(f"Average is ${average:,.2f}")

      
    