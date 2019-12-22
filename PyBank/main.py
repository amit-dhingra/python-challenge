# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# the file to write to
output_path = os.path.join("results.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Get the header row so that it can be skipped
    next(csvreader)

    #Get the first row of the file in a first_row variable
    first_row=next(csvreader)

    # ------------------------------------------
    # Set variable to 1 since we have already read one row
    total_number_months = 1

    total_change = 0


    net_total_amount = int(first_row[1])
    previous_row_amount = int(first_row[1])
    greatest_increase = 0
    greatest_increase_row = 0
    greatest_decrease = 0
    greatest_decrease_row = 0

    # Loop through the file
    for row in csvreader:
        total_number_months = total_number_months + 1
        net_total_amount = net_total_amount + int(row[1] )
        total_change = total_change + int(row[1]) - previous_row_amount
        #print(int(row[1])-previous_row_amount)
        if (int(row[1])-previous_row_amount) >greatest_increase:
            greatest_increase = int(row[1])-previous_row_amount
            greatest_increase_row=row[0]

        if (int(row[1])-previous_row_amount) <greatest_decrease:
            greatest_decrease = int(row[1])-previous_row_amount
            greatest_decrease_row=row[0]

        previous_row_amount = int(row[1])

    average = total_change/(total_number_months-1)
    average = round(average,2)



    print("Financial Analysis")
    print("-----------------------------")
    print(f'Total Months: {total_number_months}')
    print(f'Total : ${net_total_amount}')
    print(f'Average  Change: ${average}')
    print(f'Greatest Increase in Profits: {greatest_increase_row} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_row} (${greatest_decrease})')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile1:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile1, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f'Total Months: {total_number_months}'])
    csvwriter.writerow([f'Total : ${net_total_amount}'])
    csvwriter.writerow([f'Average  Change: ${average}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_row} (${greatest_increase})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_row} (${greatest_decrease})'])
