# Retrieve the data 
# Total number of votes cast
# Name of the candidates
# % of votes won by each candidate
# Total number of votes candidates won
# Winner of elections by popular vote

import csv

import os

# Assign a variable to load the file and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total vote count
total_votes = 0

# Candidate options
candidate_options = []

# declare an empty dictionary
candidate_votes = {}

# declare winning cadidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    
    # print each row in the csv file
    for row in file_reader:
       
        # Add to the total vote count
         total_votes += 1

         # Print candidate name
         candidate_name = row[2]

        # if the candidate does not match an existing candidate
         if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
           
         # Track the candidate votes
            candidate_votes[candidate_name] = 0

        
        # Add a vote to that candidate count
         candidate_votes[candidate_name] += 1

# iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a cadidate
    votes = candidate_votes[candidate_name]

    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # print th candidate name and percentage votes
    # print(f"{candidate_name} recieved {vote_percentage:.2f} % of the vote.")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
        
    print(f"{candidate_name} : {vote_percentage:.1f} % ({votes:,})\n")
    
    
winning_candidate_summary = (
        f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage : {winning_percentage:.1f}\n"
        f"--------------------------------\n")

print(winning_candidate_summary)
# Use the open statement to open the file as a text file.
#with open(file_to_save , "w") as txt_file:

# Write 3 counties to the file.
 #   txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


