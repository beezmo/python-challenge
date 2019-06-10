import csv

#initialize variables
totalMonths = 0
netTotal = 0
maxProfit = 0.0
maxProfitDate = ""
maxLoss = 0.0
maxLossDate = ""
profitChangeList = []
lineCount = True

with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for rows in csvreader:

        #Gets first profit entry
        if lineCount:
            lastMonth = int(rows[1])
            lineCount = False

        #Tracks number of rows (=months)
        totalMonths += 1
        #Calculates total
        netTotal += int(rows[1])

        #Calculates change in profit, appends to list, then sets up for next line
        profitChange = int(rows[1]) - lastMonth
        profitChangeList.append(profitChange)
        lastMonth = int(rows[1])

        #Determines if current profit change is greatest value thus far
        if profitChange > maxProfit:
            maxProfit = profitChange
            maxProfitDate = rows[0]
        
        #Determines if current profit change is least thus far
        if profitChange < maxLoss:
            maxLoss = profitChange
            maxLossDate = rows[0]

#Total profit change divided by (length - 1) to account for initial 0
avgChange = round(sum(profitChangeList) / (len(profitChangeList) - 1), 2)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Amount: {netTotal}")
print(f"Average Change: {avgChange}")
print(f"Greatest Increase in Profits: {maxProfitDate} (${maxProfit})")
print(f"Greatest Decrease in Profits: {maxLossDate} (${maxLoss})")

f = open("PyBankAnalysis.txt", "w+")
print("Financial Analysis", file=f)
print("---------------------------", file=f)
print(f"Total Months: {totalMonths}", file=f)
print(f"Total Amount: {netTotal}", file=f)
print(f"Average Change: {avgChange}", file=f)
print(f"Greatest Increase in Profits: {maxProfitDate} (${maxProfit})", file=f)
print(f"Greatest Decrease in Profits: {maxLossDate} (${maxLoss})", file=f)
f.close()