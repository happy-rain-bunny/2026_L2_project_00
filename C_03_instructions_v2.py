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
    make_statement(statement="Instructions", decoration="ℹ️")

    # Initialise ticket numbers
    MAX_TICKETS = 5
    tickets_sold = 0

    while tickets_sold < MAX_TICKETS:
        name = input("Name: ")

        # if name is exit code, break out of loop
        if name == "xxx":
            break

        tickets_sold += 1

    if tickets_sold == MAX_TICKETS:
        print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
    else:
        print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")


# Main routine goes here

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ",
                                 ("yes", "no"), 1)

if want_instructions=="yes":
        instructions()

print()
print("program continues...")
