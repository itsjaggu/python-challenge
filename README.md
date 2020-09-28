# python-challenge
This repository include analysis scripts for Budget Data and Election Poll Data.
## [Budget Data Analysis (PyBank)](PyBank)
The [PyBank script](PyBank/main.py) runs row by row on the csv data file available in the [Resources](PyBank/Resources) folder to analyze the data. The analysis includes following key metrics:
  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

The output of analysis is printed in the terminal window and it also get saved in a text file in [Analysis](PyBank/Analysis) folder. The output looks like following:
```text
  Financial Analysis
  -----------------------------------
  Total Months: 86
  Total: $38,382,578.00
  Average  Change: $-2,315.12
  Greatest Increase in Profits: Feb-2012 ($1,926,159.00)
  Greatest Decrease in Profits: Sep-2013 ($-2,196,167.00)
  ```
## [Election Poll Analysis (PyPoll)](PyPoll)
The [PyPoll script](PyPoll/main.py) runs row by row on the csv data file available in the [Resources](PyPoll/Resources) folder to analyze the data. The analysis includes following key metrics:
  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
  
The output of analysis is printed in the terminal window and it also get saved in a text file in [Analysis](PyPoll/Analysis) folder. The output looks like following:
```text
  Election Results
  -----------------------------------
  Total Votes: 3521001
  -----------------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -----------------------------------
  Winner: Khan
  -----------------------------------
  ```