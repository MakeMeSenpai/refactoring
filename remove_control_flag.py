"""Remove control flag"""
# by Kami Bigdely

def find_food(food, fridge):
    for item in fridge:
        if food in item:
            item_name = item
            return item_name
    return None

if __name__ == "__main__":
    food = 'wasabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barge', 'wasabi']
    found_item = find_food(food, food_list)
    print(food, "Found: " + found_item  if found_item != None else "not found")
