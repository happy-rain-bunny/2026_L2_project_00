# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full word
    of the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            #check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check(question= "Do you like coffee? ", valid_ans_list=yes_no_list, num_letters=1)
print(f"You chose {like_coffee}")
pay_method = string_check(question="Payment method: ", valid_ans_list=payment_list, num_letters=2)
print(f"You chose {pay_method}")