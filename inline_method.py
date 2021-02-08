"""This module checks if a person can enter a night club/drink"""

DRINKING_AGE = 18
MY_AGE = 17.9

def enter_night_club():
    """prints if a person is old enough"""
    if MY_AGE >= DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Entrance of minors is denied.")

enter_night_club()
