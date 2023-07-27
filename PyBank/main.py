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
    date = []

    #read through each row and count the months and sum of profit losses
    for rows in csv_reader:
        rowcount.append(rows[0])
        nettotal.append(int(rows[1]))
        totalnumbermonths = len(rowcount)
        date.append(rows[0])
    #changes in "Profit/Losses"
        changed = int(rows[1]) - previous
        previous = int(rows [1]) 
        changedrevenue.append(changed)
    changedrevenue.pop(0)
    average = sum(changedrevenue)/(totalnumbermonths-1) 
    nettotal = int(sum(nettotal))
# greatest increase and decrease in revenue
    greatest_increase = max(changedrevenue)
    greatest_decrease = min(changedrevenue)
    IncreaseDate = date[changedrevenue.index(greatest_increase)+1]
    DecreaseDate = date[changedrevenue.index(greatest_decrease)+1]

#Print results
    print("Financial Analysis")
    print("------------------------------")
    print(f" Total number of months {totalnumbermonths}")
    print(f"Total ${nettotal}")
    print(f"Average Change is ${average:,.2f}")
    print(f"Greatest Increase in Profits: {IncreaseDate} ${max(changedrevenue)}")
    print(f"Greatest Decrease in Profits: {DecreaseDate} ${min(changedrevenue)}")


file = 'Pybank','analysis', 'AnalysisResults.txt'
with open(file, 'w') as text:
    file.write("Financial Analysis" + "\n")
    file.write("-----------------------------------------" + "\n")
    file.write(" Total number of months {totalnumbermonths}")
    file.write("Total ${nettotal}")
    file.write("Average Change is ${average:,.2f}")
    file.write("Greatest Increase in Profits: {IncreaseDate} ${max(changedrevenue)}")
    file.write("Greatest Decrease in Profits: {DecreaseDate} ${min(changedrevenue)}")
file.close()  
    