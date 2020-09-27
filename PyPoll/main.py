import os
import csv

# Getting path for csv data file
csvpath = os.path.join("Resources","election_data.csv")

def getunique(datalist):
    unique_list = []
    for x in datalist:
        if x not in unique_list:
            unique_list.append(x)

# Reading csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalvotes = 0
    candidates = []

    for row in csvreader:
    # The total number of votes cast
    #totalvotes = sum(1 for row in csvreader)
        totalvotes = totalvotes + 1

    # A complete list of candidates who received votes
    #for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])

        # The percentage of votes each candidate won
        
        # The total number of votes each candidate won
        
        # The winner of the election based on popular vote.
        

    #avgchangeamountdollar = "${:,.2f}".format(sum(avgchange)/len(avgchange))
    
    print(f"Total Votes: {totalvotes}")
    print(candidates)

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------