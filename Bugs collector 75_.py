# Bug Collector
# October 8 2018
# CTI-110 P4T2 - Bug Collector
# Johnson Jordan
#
 #Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range (1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

    #Display the total bugs.
    print('You Collected a total of', total,'bugs.')
    
