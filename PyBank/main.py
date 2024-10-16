# Modules
import os
import csv


# Set path for file.
csvpath=os.path.join("Resources","budget_data.csv")


# open the csv file UTF-8 encoding.
with open(csvpath,encoding="UTF-8") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
   
    # read the header row first.
    csv_header=next(csv_reader)
    
    # Read all data after the header all data convert in list.
    data=list(csv_reader)
    
    # Read first column data after the header.
    total_month=[row[0] for row in data]

    # Get list which has only month contain.
    month = [row[0].split("-")[0] for row in data]
   
    # Get list which contain profit and loss data.
    profit_losses=[int(row[1]) for row in data]

    
    # Loop through calculate the total of profit and loss.
    net_amout=0
    for net in data:
        net_amout+=int(net[1])


    total_change=0
    count=0
    increase_profit=0
    decrease_profit=0
    increase_date=""
    decrease_date=""
    # Loop through calculate the increase an decrease profit and according that date also.
    for value in range(1,len(profit_losses)):
        change=profit_losses[value]-profit_losses[value-1]
        total_change+= change
        count+=1


        if change>increase_profit:
            increase_profit=change
            increase_date=total_month[value]

        if change<decrease_profit:
            decrease_profit=change
            decrease_date=total_month[value]

        

    # check the average change of profit and loss.
    if count>0:
        average_change=total_change/count
    else:
        average_change=0

# Display output in the terminal
print("\nFinancial Analysis\n")
print("\n--------------------------------------\n")
print(f"\nTotal Months: {len(month)}\n")
print(f"\nTotal: ${net_amout}\n")
print(f"\nAverage Change: ${average_change:.2f}\n")
print(f"\nGreatest Increase in Profits {increase_date} $({increase_profit})\n")
print(f"\nGreatest Increase in Profits {decrease_date} $({decrease_profit})\n")




# Export a result in text file
with open('analysis/analysis_result_of_PyBank.txt', 'w') as file:
    file.write("\nFinancial Analysis\n")
    file.write("\n---------------------------------------\n")
    file.write(f"\nTotal Months: {len(month)}\n")
    file.write(f"\nTotal: ${net_amout}\n")
    file.write(f"\nAverage Change: ${average_change:.2f}\n")
    file.write(f"\nGreatest Increase in Profits {increase_date} $({increase_profit})\n")
    file.write(f"\nGreatest Increase in Profits {decrease_date} $({decrease_profit})\n")
