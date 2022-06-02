# Card Intake Application (CIA)
# This program will allow a user to do the following:
# [ ] Input new card information (via a new/existing text file aka the 'database')
# [ ] Search through their card collection (via an existing text file)
# [ ] Delete cards from their collection
# [ ] Modify specific information on an existing card's data

# Declaring Variables
card_name = null
card_set_num = 0
if_holo = false
card_region = null

# Main Function
def main():
    user_action = input('What would you like to do with your card collection today? (choose add, delete, or edit) ')

    while True:
        try:
            if user_action == 'add':
                # insert add function here
            elif user_action == 'delete':
                # insert delete function here
            elif user_action == 'edit':
                # insert edit function here
            else:
                user_action = input('Invalid input, try again. (choose add, delete, or edit) ')
        except:
            user_action = input('Invalid input, try again. (choose add, delete, or edit) ')

# Adding New Cards
def add_cards():

# Deleting Existing Cards

# Editing Existing Cards

# starting over again