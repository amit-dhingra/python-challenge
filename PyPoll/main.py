# Modules
import os
import csv
import random


# Set path for file
csvpath = os.path.join("election_data.csv")
# the file to write to
output_path = os.path.join("PyPoll_results.csv")

candidate_list=[]
candidate_votes_list=[]
candidate_votes=0
i=0
percent_votes = 0.00
percent_votes_winner = 0.00
winner='A'




#csvreader1 = csv.reader(csvfile, delimiter=",")
#next(csvreader1)

# Open the CSV
with open(csvpath, newline="") as csvfile:


    #Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=",")

    #Get the header row so that it can be skipped
    next(csvreader)

    #Get the first row of the file in a first_row variable
    first_row=next(csvreader)

    # ------------------------------------------
    # Set variable to 1 since we have already read one row
    total_number_votes = 1
    previous_candidate = first_row[2]
    candidate_list.append(previous_candidate)


    # Loop through the file
    for row in csvreader:
        current_candidate = row[2]
        if current_candidate not in candidate_list:
            candidate_list.append(current_candidate)
        total_number_votes = total_number_votes+1

for row in candidate_list:
    candidate_votes = 0
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row1 in csvreader:
            if row == row1[2]:
                candidate_votes= candidate_votes +1
    candidate_votes_list.append(candidate_votes)


#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile1:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile1, delimiter=',')

    print("Election Results")
    csvwriter.writerow(["Election Results"])
    print("-----------------------------")
    csvwriter.writerow(['-----------------------------'])
    print(f'Total Votes: {total_number_votes}')
    csvwriter.writerow([f'Total Votes: {total_number_votes}'])
    print("-----------------------------")
    csvwriter.writerow(['------------------------------'])
    for row in candidate_list:
        percent_votes = (candidate_votes_list[i]/total_number_votes)*100.00
        if(percent_votes_winner < percent_votes ):
            winner = row
            percent_votes_winner=percent_votes

        print(f'{row} :{percent_votes:.3f}% ({candidate_votes_list[i]})')

        csvwriter.writerow([f'{row} :{percent_votes:.3f}% ({candidate_votes_list[i]})'])

        i = i+1
    print("-----------------------------")
    csvwriter.writerow(['-----------------------------'])
    print(f'Winner :{winner} ')
    csvwriter.writerow([f'Winner :{winner}'])
    print("-----------------------------")
    csvwriter.writerow(['-----------------------------'])
