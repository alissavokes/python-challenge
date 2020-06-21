import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

month_counter = 0
net_PL = 0
prior_month_PL = 0
changes_list =[]
changes_by_month = {}

with open(csvpath) as budget_data_csv:
    read_budget_data = csv.reader(budget_data_csv, delimiter=',')
    next(budget_data_csv)
    for row in read_budget_data:
        profit_loss = int(row[1])
        #counting each row after header for count of total months
        month_counter = month_counter + 1
        #summing P/L for each month
        net_PL += profit_loss
        #calculating difference between prior month's PL and current month's PL
        change = profit_loss - prior_month_PL
        #adding change to list to keep track
        changes_list.append(change)
        #attaching each change to corresponding month
        changes_by_month[change] = row[0]
        #updating prior_month_PL to current row for next iteration
        prior_month_PL = int(row[1])
    
    #remove first value in list as there is no prior month to reference for Jan 2010
    changes_list.pop(0)
    #calculate average change
    average_changes = round(sum(changes_list)/len(changes_list), 2)
    #calculate greatest increase
    max_change = max(changes_list)
    max_change_month = changes_by_month[max_change]
    #calculate greatest decrease
    min_change = min(changes_list)
    min_change_month = changes_by_month[min_change]

#analysis terminal output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Total: ${net_PL}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

output_file = os.path.join("Analysis", "financial_analysis.txt")
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {month_counter}\n")
    datafile.write(f"Total: ${net_PL}\n")
    datafile.write(f"Average Change: ${average_changes}\n")
    datafile.write(f"Greatest Increase in Profits: {max_change_month} (${max_change})\n")
    datafile.write(f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n")