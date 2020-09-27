import os
import csv

# Getting path for csv data file
csvpath = os.path.join("Resources","budget_data.csv")

# Reading csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalmonths = 0
    totalamount = 0
    greatestincrease = 0
    greatestincreasemonth = ""
    greatestdecrease = 0
    greatestdecreasemonth = ""

    for row in csvreader:
        amount = float(row[1])
        # The total number of months included in the dataset
        totalmonths = totalmonths + 1

        # The net total amount of "Profit/Losses" over the entire period
        totalamount = totalamount + amount

        # The greatest increase in profits (date and amount) over the entire period
        if amount > greatestincrease:
            greatestincrease = amount
            greatestincreasemonth = str(row[0])

        # The greatest decrease in losses (date and amount) over the entire period
        if amount < greatestdecrease:
            greatestdecrease = amount
            greatestdecreasemonth = str(row[0])
    
    totalamountdollar = "${:,.2f}".format(totalamount)
    greatestincreasedollar = "${:,.2f}".format(greatestincrease)
    greatestdecreasedollar = "${:,.2f}".format(greatestdecrease)
    print(totalmonths)
    print(totalamountdollar)
    print(f"Greatest Increase in Profits: {greatestincreasemonth} ({greatestincreasedollar})")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} ({greatestdecreasedollar})")

# The average of the changes in "Profit/Losses" over the entire period

# Final Output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)