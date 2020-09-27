import os
import csv

# Getting path for csv data file
csvpath = os.path.join("Resources","budget_data.csv")

# Output text file path
outputtext = os.path.join("Analysis","PyBank_Result.txt")

# Reading csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Initializing variables
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

    # Reading rows of csv data file
    for row in csvreader:
        curramount = float(row[1])

        # The total number of months included in the dataset
        totalmonths = totalmonths + 1

        # The net total amount of "Profit/Losses" over the entire period
        totalamount = totalamount + curramount

        # Setting precious row amount and computing change in amount
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

# converting amount format to currency for output  
avgchangeamountdollar = "${:,.2f}".format(sum(avgchange)/len(avgchange))
totalamountdollar = "${:,.2f}".format(totalamount)
greatestincreasedollar = "${:,.2f}".format(greatestincrease)
greatestdecreasedollar = "${:,.2f}".format(greatestdecrease)

# Saving the results in text file and printing in terminal
saveresult = open(outputtext,"w")
print("Financial Analysis")
saveresult.write("Financial Analysis" + "\n")
print("-----------------------------------")
saveresult.write("-----------------------------------" + "\n")
print(f"Total Months: {totalmonths}")
saveresult.write(f"Total Months: {totalmonths}" + "\n")
print(f"Total: {totalamountdollar}")
saveresult.write(f"Total: {totalamountdollar}" + "\n")
#print(f"Length: {len(avgchange)}")
print(f"Average  Change: {avgchangeamountdollar}")
saveresult.write(f"Average  Change: {avgchangeamountdollar}" + "\n")
print(f"Greatest Increase in Profits: {greatestincreasemonth} ({greatestincreasedollar})")
saveresult.write(f"Greatest Increase in Profits: {greatestincreasemonth} ({greatestincreasedollar})" + "\n")
print(f"Greatest Decrease in Profits: {greatestdecreasemonth} ({greatestdecreasedollar})")
saveresult.write(f"Greatest Decrease in Profits: {greatestdecreasemonth} ({greatestdecreasedollar})")
saveresult.close()