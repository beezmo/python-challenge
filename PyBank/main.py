import os
import csv

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
        if lineCount:
            lastMonth = int(rows[1])
            lineCount = False

        totalMonths += 1
        netTotal += int(rows[1])
        profitChange = int(rows[1]) - lastMonth
        profitChangeList.append(profitChange)
        lastMonth = int(rows[1])

        if profitChange > maxProfit:
            maxProfit = profitChange
            maxProfitDate = rows[0]
        
        if profitChange < maxLoss:
            maxLoss = profitChange
            maxLossDate = rows[0]

avgChange = sum(profitChangeList) / (len(profitChangeList) - 1)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Amount: {netTotal}")
print(f"Average Change: {avgChange}")
print(f"Greatest Increase in Profits: {maxProfitDate} (${maxProfit})")
print(f"Greatest Decrease in Profits: {maxLossDate} (${maxLoss})")