# Initial variable to track game play
user_play = "y"
startnumber = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
            z = input(" How Many numbers to loop through? ")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
            for x in range(startnumber, int (z)+ startnumber):

           
    # Print each number in the range
                 print(x)

            startnumber = startnumber + int (z)

    # Once complete...
            user_play = input("Continue: (y)es or (n)o? ")
