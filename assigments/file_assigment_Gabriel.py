# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.

import json
import pickle


def get_user_input():
    user_input = input(
        'Enter your text, which you will find in the text file:')
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

my_list_json = []
my_list_pickle = []
waiting_for_input = True
while waiting_for_input:
    
    print('Please choose:')
    print('1: Add  text to a file')
    print('2: Read the content of the file')
    print('3: Store user input in a list and stored into a file based on json.')
    print('4: Store user input in a list and stored into a file based on pickle.')
    print('5: Read user input from a list based on json.')
    print('6: Read user input from a list based on pickle.')
    print('q: Exit')

    user_choice = get_user_choice()
    
    if user_choice == '1':
        user_input = get_user_input()
        with open('file_assignment.txt', mode='w') as f:
            f.write(user_input)
    elif user_choice == '2':
        with open('file_assignment.txt', mode='r') as f:
            line = f.readline()
            while line:
                print(line)
                line = f.readline()

    elif user_choice == '3':
        user_input = get_user_input()
        my_list_json.append(str(user_input))
        print(my_list_json)
        with open('file_assignment_list_json.txt', mode='a') as f:            
            f.write(json.dumps(my_list_json))

    elif user_choice == '4':
        user_input = get_user_input()
        my_list_pickle.append(str(user_input))
        with open('file_assignment_list_pickle.txt', mode='ab') as f:            
            f.write(pickle.dumps(my_list_pickle))
    
    elif user_choice == '5':
        with open('file_assignment_list_json.txt', mode='r') as f:
            file_content = f.readline()
           # print(file_content)
            my_list_json = json.loads(file_content)
            print(my_list_json)
            for line in my_list_json:
                print(line)


    elif user_choice == '6':
        with open('file_assignment_list_pickle.txt', mode='rb') as f:
            my_list_pickle = pickle.loads(f.read())
            print(my_list_pickle)
            


    elif user_choice == 'q':
        waiting_for_input = False


