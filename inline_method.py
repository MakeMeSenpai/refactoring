drinking_age = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(individual):
    if individual.age >= drinking_age:
        print("Allowed to enter.")
    else: 
        print("Entrance of minors is denied.")
    
    
person = Person(17.9)
enter_night_club(person)
