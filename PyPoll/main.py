import csv

#initialize variables
totalVotes = 0
candidateVotes = 0
candidatesList = []
votesList = []

with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for rows in csvreader:

        #Tracks number of rows (= total votes)
        totalVotes += 1
        #If candidate is not in list, append new candidate name and also append 1 vote to votesList
        #Else find index of candidate in list and add one vote to corresponding entry in votesList
        if rows[2] not in candidatesList:
            candidatesList.append(rows[2])
            votesList.append(1)
        else:
            votesList[candidatesList.index(rows[2])] += 1