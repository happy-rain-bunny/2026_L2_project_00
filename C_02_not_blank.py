def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        responses = input(question).strip()
        if responses != "":
            return responses

        print("Sorry, this can't be blank. Please try again.\n")


# main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")