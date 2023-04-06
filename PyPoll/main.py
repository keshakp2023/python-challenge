import os
import csv

# pulling data from csv file  
csvpath = os.path.join('..','PYPOLL','Resources', 'election_data.csv')

with open(csvpath, "r") as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #define variable

    Total_Votes = 0 
    candidate_index = []
    Number_votes = dict()

    print ("Election Results")
    print ("----------------------------")

    # calculate total number of votes 

    for row in csvreader:
        Total_Votes += 1
    
        candidate_1 = row[2]
        if candidate_1 not in candidate_index:
            candidate_index.append(candidate_1)
            Number_votes[candidate_1] = 0

        Number_votes[candidate_1] += 1      

    print("Total Votes:", Total_Votes ) 
    print("----------------------------")

    #calcualating per candidate's votes and percentage 
    for candidate_1 in Number_votes:
        votes = Number_votes[candidate_1]
        vote_percentage = round ((100 * float(votes)/float(Total_Votes)),3)

        candidate_result = (f"{candidate_1}: {vote_percentage}% ({votes:})\n")
        print(candidate_result)



        winner = (max(Number_votes, key=Number_votes.get))
    #result 
    print("----------------------------")
    print("Winner:", winner)
    print("----------------------------")

#Export data to text file
with open(os.path.join("Analysis", "output-file.txt"), "w") as textfile:
    textfile.write ("Election Results\n")
    textfile.write ("----------------------------\n")
    textfile.write(f"Total Votes:{Total_Votes}\n" ) 
    textfile.write ("----------------------------\n")        

    for candidate_1 in Number_votes:
        votes = Number_votes[candidate_1]
        vote_percentage = round ((100 * float(votes)/float(Total_Votes)),3)

        candidate_result = (f"{candidate_1}: {vote_percentage}% ({votes:})\n")
        textfile.write(f"{candidate_result}")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("----------------------------\n")

    
   
   
   

        
       