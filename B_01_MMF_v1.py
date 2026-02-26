# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3}{statement}{decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    of the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            #check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    print()
    make_statement(statement="Instructions", decoration="ℹ️")

    print("""
    This is the first instruction. 
    And the second instructions. 

    So now you can use the program. 

    """)

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        responses = input(question).strip()
        if responses != "":
            return responses

        print("Sorry, this can't be blank. Please try again.\n")


def int_check(question):
    """Checks users enter an integer"""

    error = "Please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)



# Main routine goes here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# Intialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')


make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ",
                                 ("yes", "no"), 1)

if want_instructions=="yes":
        instructions()

print()

while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"Sorry you are too young for this movie\n")
        continue
    elif age > 120:
        print(f"??That looks like a type (too old)\n")
        continue

    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})\n")
    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")

