import csv

#initialize variables
totalVotes = 0
candidatesList = []
votesList = []
percentList = []

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

#creates list of each candidate's vote percentage
percentList = ["{0:.03%}".format(votes/totalVotes) for votes in votesList]

#determines winner by finding most votes in votesList, then matches index with name in candidatesList
winner = candidatesList[votesList.index(max(votesList))]

#zip candidates together with vote counts and percentages into dictionary
zipResults = zip(candidatesList, percentList, votesList)
results = list(zipResults)

#terminal output
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------")
for x in results:
    print(x[0] + ": " + str(x[1]) + " (" + str(x[2]) + ")")
print("---------------------------")
print(f"Winner: {winner}")

#txt output
f = open("PyPollResults.txt", "w+")
print("Election Results", file=f)
print("---------------------------", file=f)
print(f"Total Votes: {totalVotes}", file=f)
print("---------------------------", file=f)
for x in results:
    print(x[0] + ": " + str(x[1]) + " (" + str(x[2]) + ")", file=f)
print("---------------------------", file=f)
print(f"Winner: {winner}", file=f)
f.close()