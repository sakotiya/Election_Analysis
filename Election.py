
import datetime
now = datetime.datetime.now()
print("time", now)



my_votes = int(input("How many votes did you get in election?"))
total_votes = int(input("How many total votes in the election?"))
percentage_votes = my_votes/total_votes *100
print("I received " +str(percentage_votes)+ " % of the total votes")


temperature = int(input("what is the tempturee outside?"))

if temperature > 80:
        print("Too Hot")
else:
        print("Lets go outside ")


Score = int(input("What is the score ?"))

if Score > 90:
    print("Grade is A")
elif Score >= 80:
    print("B")
elif Score >=70:
    print("C")
elif Score >60:
    print("D")
else:
    print("Fail")

    x = 0
    while x <= 5:
        print(x)
        x = x+1

    numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
    
for num in range(10):
    print(num)

counties = ["sd", "df", "er", "fd"]
for i in range(len(counties)):
    print(counties[i])


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    printf = {(f"{county} county has {voters} registered voters.")



