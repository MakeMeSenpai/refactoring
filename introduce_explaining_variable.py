"""Split temp variable"""
# By Kami Bigdely

def save_into_db():
    """print response to user"""
    user_input = input('Please enter your username: ')
    user_input = int(input('Please enter your birth year: '))
    print("saved into database")
    age = 2020 - user_input
    print("You are",age, "years old.")
