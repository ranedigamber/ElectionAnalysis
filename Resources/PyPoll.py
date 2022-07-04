#Add our dependencies
import csv
import os

# Assign a variable to the file to load and its path
file_to_load=os.path.join("Resources","election_results.csv")
# The data that we need to retrieve
with open(file_to_load) as election_data:
#To do: perform analysis
#    print(election_data)
#Create a filename variable to a direct or indirect path to the file
    file_to_save=os.path.join("analysis", "election_analysis.txt")
# using the open() function with the "w" mode we will write data to the file
##with open(file_to_save, "w") as txt_file:
# write something in the file
#    txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson") 

#To do: read and analyze the data here

# Read the file object with the reader function
file_reader=csv.reader(election_data)

#print each row in the CSV file
for row in file_reader:
    print(row)





# 1. The total number of votes cast
# 2. A list of candidates who received votes
# 3. The percentage of votes each candidate received
# 4. The total number of votes each candidate received
# 5. The winner of the election based on popular vote.



