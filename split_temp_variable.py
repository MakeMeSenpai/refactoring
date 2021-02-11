"""splitting large equations into short vars"""
# by Kami Bigdely
# Split temporary variable

def sandwich_weight(burger):
    """gets the weight of our burger"""
    patty = 70
    patty_num = 2
    buns = 95
    buns_num = 2
    plain = patty_num * patty + buns * buns_num

    pickle = 20
    pickle_num = 4

    tomatoes = 25
    tomatoes_num = 3

    lettuce = 15
    lettuce_num = 2

    golden_fried_onion = 20

    kimchi = 30
    mayo = 5

    if burger == "Seoul Kimchi Burger Weight":
        toppings = pickle_num * pickle + tomatoes_num * tomatoes + kimchi + mayo + golden_fried_onion
        return plain + toppings
    elif burger == "NY Burger Weight":
        toppings = pickle_num * pickle + tomatoes_num * tomatoes + lettuce_num * lettuce
        return plain + toppings


print("NY Burger Weight", sandwich_weight("NY Burger Weight"))
print("Seoul Kimchi Burger Weight", sandwich_weight("Seoul Kimchi Burger Weight"))
