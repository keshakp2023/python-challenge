import os
import csv

# pulling data from csv file 
csvpath = os.path.join('.','Resources', 'budget_data.csv')

with open(csvpath, "r") as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')

    print ("Financial Analysis")
    
    print ("----------------------------")

    csv_header = next(csvreader)

    #define Variable
 
    Total_months= 0
    net_total= 0
    revenue_diff = 0

    list_of_revenue = []
    greatest_value_increase = 0
    greatest_value_decrease = 0

    #finding total number of months by finding total number of rows
    
    for index, row in enumerate(csvreader):
        Total_months += 1 
        net_total += int(row[1])
        if index == 0 :
            previous_revenue = int(row[1])
        else:
            revenue_diff = int(row[1])- previous_revenue
            previous_revenue = int(row[1])
            list_of_revenue.append(revenue_diff)

        #finde average change and greatest increase and decrease percentage 

        if greatest_value_increase < revenue_diff:
            greatest_value_increase = revenue_diff
            greatest_date_increase = row[0]

        if greatest_value_decrease > revenue_diff:
            greatest_value_decrease = revenue_diff
            greatest_date_decrease = row[0]

revenue_average = sum(list_of_revenue)/len(list_of_revenue)

# Print Result       
print(f"Total Months: {Total_months}") 
print(f"Total: $ {net_total}")  
print(f"Average Change: $ {revenue_average}") 
print(f"Greatest Increase in Profits: {greatest_date_increase} ${greatest_value_increase}") 
print(f"Greatest Decrease in Profits: {greatest_date_decrease} ${greatest_value_decrease}") 


# exporting to text file 

with open(os.path.join("Analysis", "output-file.txt"), "w") as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"----------------------------\n")
    textfile.write(f"Total Months: {Total_months}\n") 
    textfile.write(f"Total: $ {net_total}\n")  
    textfile.write(f"Average Change: $ {revenue_average}\n") 
    textfile.write(f"Greatest Increase in Profits: {greatest_date_increase} ${greatest_value_increase}\n") 
    textfile.write(f"Greatest Decrease in Profits: {greatest_date_decrease} ${greatest_value_decrease}\n") 
