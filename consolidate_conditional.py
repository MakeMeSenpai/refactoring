"""Consolidate conditional expressions"""
# by Kami Bigdely

def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def make_shiraz_salad(ingredients):
    if ingredients != ['cucumber', 'tomato', 'lemon juice', 'onion']:
        print("Lack of ingredients")
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shiraz salad is ready!')

if __name__ == "__main__":
    make_shiraz_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
