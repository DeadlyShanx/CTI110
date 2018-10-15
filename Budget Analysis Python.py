# Budget Analysis
# September 25 2018
# CTI-110 P4HW1 - Budget Analysis
# Johnson Jordan
#
userBudget = float(input('Please enter how much you have budgeted '+\
                         'for the month:'))
moreExpenses='y'
userTotalExpenses = 0
while moreExpenses == 'y':
    userExpense = float(input('Enter an expense:'))
    userTotalExpenses+=userExpense
    moreExpenses=input('Do you have more expenses?: Type y\
                       for yes,n for no:')
if userTotalExpenses > userBudget:
    print('You were over your budget of','$'+ format(userBudget,',.2f'),\
          'by $',format(userBudget-userTotalExpenses,',.2f'))
elif userBudget>userTotalExpenses:
    print('You were under your budget of','$'+format(userBudget,',.2f'),\
          'by','$'+format(userBudget-userTotalExpenses,',.2f'))
else:
    print('You used exactly your budget of',\
          '$'+format(userBudget,',.2f'),'.')
