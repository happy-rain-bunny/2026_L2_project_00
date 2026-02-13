# Functions go here
from http.client import responses


def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    of the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            #check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check(question= "Do you like coffee? ", valid_ans_list= ['yes', 'no'])
print(f"You chose {like_coffee}")

choose_level = string_check(question= "Choose a level: ", valid_ans_list= levels)

# Print the chosen level
print(f"You chose {choose_level}")