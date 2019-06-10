import csv

#initialize variables
totalVotes = 0
candidateVotes = 0
candidates = []

with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for rows in csvreader:

        #Tracks number of rows (= total votes)
        totalVotes += 1
        #
        if rows[2] not in candidates:
            candidates.append(rows[2])
    print(candidates)