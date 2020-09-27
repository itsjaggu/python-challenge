import os
import csv

# Getting path for csv data file
csvpath = os.path.join("Resources","budget_data.csv")

# Reading csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period
    totalmonths = 0
    totalamount = 0
    greatestincrease = 0
    greatestincreasemonth = ""
    for row in csvreader:
        amount = float(row[1])
        totalmonths = totalmonths + 1
        totalamount = totalamount + amount
        if amount > greatestincrease:
            greatestincrease = amount
            greatestincreasemonth = str(row[0])
        
    totalamountdollar = "${:,.2f}".format(totalamount)
    print(totalmonths)
    print(totalamountdollar)
    print

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period



# Final Output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)