# Modules
import os
import csv


# Set path for file
csvpath=os.path.join("Resources","election_data.csv")


# open the csv file UTF-8 encoding.
with open(csvpath,encoding="UTF-8") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    
    # Read the header row first.
    csv_header=next(csv_reader)
   

    # Read all data after the header all data convert in list.
    data=list(csv_reader)


    total_votes=0
    candidate_votes={}
    # Loop through calculate the total votes and get candidates name and check the votes according each candidate name.
    for row in data:
        total_votes+=1
        candidate_name=row[2]  

        if candidate_name in candidate_votes:
             candidate_votes[candidate_name]+=1
        else:
             candidate_votes[candidate_name]=1
    

# Display output in the termial.
print("\nElection Results\n")
print("\n---------------------\n")
print(f"\nTotal Votes: {total_votes}\n")
print("\n---------------------\n")
maximum_vote=0
winner=""
# Here loop through we get candidate,votes total and and their percentage using  dictionary formate
for candidate,vote in candidate_votes.items():
     vote_percentage=(vote/total_votes)*100
     print(f"\n{candidate}: {vote_percentage:.3f}% ({vote})\n")

     #check the maximum vote for the winner
     if vote>maximum_vote:
          maximum_vote=vote
          winner=candidate
print("\n---------------------\n")
print(f"\nWinner: {winner}\n")
print("\n---------------------\n")


# Export a result in text file
with open('analysis/analysis_result_of_PyPoll.txt', 'w') as file:
     file.write("\nElection Results\n")
     file.write("\n----------------------\n")
     file.write(f"\nTotal Votes: {total_votes}\n")
     file.write("\n----------------------\n")
     maximum_vote=0
     winner=""
     # Here loop through we get candidate,votes total and and their percentage using  dictionary formate
     for candidate,vote in candidate_votes.items():
          vote_percentage=(vote/total_votes)*100
          file.write(f"\n{candidate}: {vote_percentage:.3f}% ({vote})\n")

          #check the maximum vote for the winner
          if vote>maximum_vote:
               maximum_vote=vote
               winner=candidate
     file.write("\n----------------------\n")
     file.write(f"\nWinner: {winner}\n")
     file.write("\n----------------------\n")


