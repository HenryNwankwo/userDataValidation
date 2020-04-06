import random
import string


# container containing user details
user_details_list = []


# a function that prints out the collected details
def print_collected_details(collected_details):
    for the_values in collected_details:

        print(f"--------------------------------------")
        print(f"FIRST NAME: {str(the_values['first_name']).upper()}")
        print(f"LAST NAME:  {str(the_values['last_name']).upper()}")
        print(f"EMAIL:      {str(the_values['email']).lower()}")
        print(f"PASSWORD:   {the_values['password']}")

    return


# a function that generates a random password for the user
def generate_random_password(first_name, last_name, string_length):
    # getting the first two and last two letters of user's first name and last name
    first_name_first2letters = first_name[0:2]
    last_name_last2letters = last_name[-2:]

    # generating random strings
    random_letter = string.ascii_letters
    random_strings = "".join(random.choice(random_letter) for i in range(string_length))

    # creating random password
    random_password = first_name_first2letters + last_name_last2letters + random_strings

    return random_password


# a function that prints user details
def printing_user_details(user_details):
    print(f"First Name: {user_details['first_name'].upper()}")
    print(f"Last Name: {user_details['last_name'].upper()}")
    print(f"Email: {user_details['email']} \nPassword: {user_details['password']}")

    return


# Verifying if user is satisfied with password
def verify_password_satisfaction_yes(password_satisfaction_answer, random_user_password):

    if password_satisfaction_answer.upper() == 'YES':

        # container containing user details
        user_details1 = {
            "first_name": user_first_name,
            "last_name": user_last_name,
            "email": user_email,
            "password": random_user_password
        }

        printing_user_details(user_details1)

        return user_details1


def verify_password_satisfaction_no(password_satisfaction_answer):
    user_details = None
    if password_satisfaction_answer.upper() == 'NO':

        user_password = input('Enter your desired password: ')

        password_length = 7
        if len(user_password) < password_length:
            print('Input a new password equal to or greater than 7 in length')
            user_password = input('Enter your desired password: ')

            # container containing user details
            user_details = {
                "first_name": user_first_name,
                "last_name": user_last_name,
                "email": user_email,
                "password": user_password
            }

            printing_user_details(user_details)
        else:
            # container containing user details
            user_details = {
                "first_name": user_first_name,
                "last_name": user_last_name,
                "email": user_email,
                "password": user_password
            }

            printing_user_details(user_details)
    return user_details


while True:
    # Getting user data
    user_first_name = input('Enter your first name: ')
    user_last_name = input('Enter your last name: ')
    user_email = input('Enter your email address: ')
    user_password = None

    user_password = generate_random_password(user_first_name, user_last_name, 5)

    print(f'This is your password: {user_password}')

    # Determining if user is satisfied with password generated
    password_satisfaction = input('Are you satisfied with this password? Type Yes or No: ').upper()

    if password_satisfaction == 'YES':
        output1 = verify_password_satisfaction_yes(password_satisfaction, user_password)
        # saving user details into list container
        user_details_list.append(output1)
        # Determining if to add another user
        command = input('To quit type QUIT, To continue type CONTINUE: ').lower()
        if command == 'quit':
            print("\n******* COLLECTED USER DETAILS *******")
            print_collected_details(user_details_list)
            print('--------------------------------------\n     You have Quit the program')
            break
        elif command == 'continue':
            continue
        else:
            command = input('WRONG INPUT!!!\nTo quit type QUIT, To continue type CONTINUE: ').lower()
            if command == 'quit':
                print_collected_details(user_details_list)
                print('You have Quit the program')
                break
            elif command == 'continue':
                continue

    elif password_satisfaction == 'NO':
        output2 = verify_password_satisfaction_no(password_satisfaction)
        # saving user details into list container
        user_details_list.append(output2)
        # Determining if to add another user
        command = input('To quit type QUIT, To continue type CONTINUE: ').lower()
        if command == 'quit':
            print_collected_details(user_details_list)
            print('You have Quit the program')
            break
        elif command == 'continue':
            continue
        else:
            command = input('WRONG INPUT!!!\nTo quit type QUIT, To continue type CONTINUE: ').lower()
            if command == 'quit':
                print_collected_details(user_details_list)
                print('You have Quit the program')
                break
            elif command == 'continue':
                continue
