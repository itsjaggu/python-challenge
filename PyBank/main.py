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
    avgchange = []
    preamount = 0
    curramount = 0
    changeamount = 0
    greatestincrease = 0
    greatestincreasemonth = ""
    greatestdecrease = 0
    greatestdecreasemonth = ""

    for row in csvreader:
        curramount = float(row[1])

        # The total number of months included in the dataset
        totalmonths = totalmonths + 1

        # The net total amount of "Profit/Losses" over the entire period
        totalamount = totalamount + curramount

        if preamount == 0:
            preamount = curramount
        else:
            changeamount = curramount - preamount
            preamount = curramount
            
        # The average of the changes in "Profit/Losses" over the entire period
        if changeamount != 0:
            avgchange.append(changeamount)

        # The greatest increase in profits (date and amount) over the entire period
        if changeamount > greatestincrease:
            greatestincrease = changeamount
            greatestincreasemonth = str(row[0])

        # The greatest decrease in losses (date and amount) over the entire period
        if changeamount < greatestdecrease:
            greatestdecrease = changeamount
            greatestdecreasemonth = str(row[0])
    
    avgchangeamountdollar = "${:,.2f}".format(sum(avgchange)/len(avgchange))
    totalamountdollar = "${:,.2f}".format(totalamount)
    greatestincreasedollar = "${:,.2f}".format(greatestincrease)
    greatestdecreasedollar = "${:,.2f}".format(greatestdecrease)
    
    print(f"Total Months: {totalmonths}")
    print(f"Total: {totalamountdollar}")
    print(f"Length: {len(avgchange)}")
    print(f"Average  Change: {avgchangeamountdollar}")
    print(f"Greatest Increase in Profits: {greatestincreasemonth} ({greatestincreasedollar})")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} ({greatestdecreasedollar})")