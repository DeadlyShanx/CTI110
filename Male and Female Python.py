# Male and Female Percentages
# September 24 2018
# CTI-110 P2HW2 - Male Female Percentage
# Johnson Jordan
#

males=int(input('Enter the Amount of Males in the Class:'))
females=int(input('Enter the Amount of Females in the Class:'))
totalstudents= males+females

malepercentage=(males/totalstudents)*100
femalepercentage=(females/totalstudents)*100
print('Male percentage:'+str(malepercentage))
print('Female percentage:'+str(femalepercentage))
