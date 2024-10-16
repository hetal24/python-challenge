# PyBank

In this Challenge, you are creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv.

## Instructions

* The task is to create a Python script that analyzes the records to calculate each of the following values:

  * The total number of months included in the dataset.

  * The net total amount of "Profit/Losses" over the entire period.

  * The changes in "Profit/Losses" over the entire period, and then the average of those changes.
  
  * The greatest increase in profits (date and amount) over the entire period.
  
  * The greatest decrease in profits (date and amount) over the entire period.

* `csv.reader` begins reading the CSV file from the first row. `next(csv_reader, None)` will skip the header row.

* Use the file.write() function to write in analysis file(Export data in the txt file).