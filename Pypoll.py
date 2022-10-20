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

# open the election results and read the file
#election_data = open(file_to_load , 'r')
with open(file_to_load,'r') as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    # print each row in the csv file
    # for row in file_reader:
    #     print(row[0])

   #print(election_data)

# close the file
#election_data.close()



# Use the open statement to open the file as a text file.
with open(file_to_save , "w") as txt_file:

# Write 3 counties to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")


