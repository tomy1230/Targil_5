import requests


def First_name():
    response = requests.get('https://randomuser.me/api/').json()
    first_name = response['results'][0]['name']['first']  #get random first name from first user spot in the dict
    return first_name


def User_value_run(number1):
    if 0 < number <= 100:
        for num in range(number1):  #for the range of the user input
            ran_user = First_name()  # use First_name class in order to get the first name 
            print(ran_user)
    elif number == -1:   
        print('You quit!')
    else:
        print("Enter number greater then 0!!!")


number=1
while number != -1: # until the user enters '-1' 
    number = int(input('Enter number between 1 - 100(enter -1 to quit):\n'))  #user input
    User_value_run(number) # send number to the class
