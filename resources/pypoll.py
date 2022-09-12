# The data we need to retrieve

#Add our dependencies
import csv
import os


# Aasign a variable to load the file from the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the data to the path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initiaze total voter count
total_votes = 0
votes = 0
wining_candidate = ""
winning_count = 0
winning_percentage = 0

#percentage of votes 
vote_percentage = 0
#Declare name of the candidates using for loop
candidate_options = []
# Create dictionery for candidate votes 

candidate_votes = {}
#open the election_data and read the file 
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

#Remove the headers from the file 

    headers = next(file_reader)
    print(headers)
  
    for row in file_reader:

    #Count total number of vptes
        total_votes= total_votes+1
       # print(total_votes)

    #print candididate name from each row
        candidate_name = row[2]
    # Add Candidate name in Candidate options 
    
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
        
        #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1
    
print(candidate_votes)
#Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}:received {vote_percentage:.2f}% of the vote")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        wining_candidate = candidate_name

        print(f"{candidate_name}:{vote_percentage:.2f}%({votes:,})\n")
wining_candidate_summary = (f"-------------------------\n"
                            f"Winner: {wining_candidate}\n"
                            f"Winning Vote Count: {winning_count:,}\n"
                            f"Winning Percentage: {winning_percentage:.1f}%\n"
                            f"-------------------------\n")
print(wining_candidate_summary)





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



