import os
import csv

# Getting path for csv data file
csvpath = os.path.join("Resources","election_data.csv")

# Output text file path
outputtext = os.path.join("Analysis","PyPoll_Result.txt")

# Reading csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Initializing variables
    totalvotes = 0
    candidate_list = []
    candidatesvotecount = dict()
    winner = ""
    winnervotes = 0

    # Reading rows of csv data file
    for row in csvreader:
    # The total number of votes cast
    # totalvotes = sum(1 for row in csvreader)
        totalvotes = totalvotes + 1

    # A complete list of candidates who received votes with vote count
    # for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidatesvotecount[row[2]] = 1
        else:
            candidatesvotecount[row[2]] = int(candidatesvotecount[row[2]]) + 1

# Saving the results in text file and printing in terminal       
saveresult = open(outputtext,"w")
saveresult.write("Election Results" + "\n")
saveresult.write("-----------------------------------" + "\n")
print(f"Total Votes: {totalvotes}")
saveresult.write(f"Total Votes: {totalvotes}" + "\n")
saveresult.write("-----------------------------------" + "\n")
for cand in candidate_list:
    percentvote = "{:,.3f}%".format((candidatesvotecount[str(cand)] / totalvotes) * 100)
    if winnervotes < candidatesvotecount[str(cand)]:
        winnervotes = candidatesvotecount[str(cand)]
        winner = cand
    print(f"{cand}: {percentvote} ({candidatesvotecount[str(cand)]})")
    saveresult.write(f"{cand}: {percentvote} ({candidatesvotecount[str(cand)]})" + "\n")
saveresult.write("-----------------------------------" + "\n")
print(f"Winner: {winner}")
saveresult.write(f"Winner: {winner}" + "\n")
saveresult.write("-----------------------------------" + "\n")
saveresult.close()