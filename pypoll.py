# The data we need to retrieve

#Add our dependencies
import csv
import os

# Aasign a variable to load the file from the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the data to the path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election_data and read the file 
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

#Remove the headers from the file 

    headers = next(file_reader)
    print(headers)


#with open(file_to_save, 'w') as outfile:
  #  outfile.write("Counties in the election\n")
  #  outfile.write("------------------------\n")
  #  outfile.write("Arapahoe\nDenver\nJefferson ")
    
#outfile.close()




# The total number of votes cast 
# A complete list of candidates who recieved votes 
# The percentage of vote each candidiate won 
# The total number of votes each candidate won 
# The winner of the election based on popular votes 



