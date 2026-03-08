import pandas
"""always need daughter frame"""

# lists to hold ticket details
all_names = ["A", "B", "C" ,"D","E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

"""create a series of lists to hold the ticket details
save some time typing -> note the speech marks, separated by commas
"""

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

"""dictionary ; the curly brackets

colon the list name and then a comma, and before next column
'Column Name' : all_list

"""

#create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

"""creates table"""

# Calculate the total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

"""match with the key from dictionary; be identical
add the values in a column using dot sum
"""

print(mini_movie_frame)

"""Worth making the list or if you want to get phython to calculate column"""

"""
exit code in the bases component but it turns out it was missing
"""