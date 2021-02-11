"""Rename Method, Reference: https://parade.com/1039985/marynliles/pick-up-lines/ """
# by Kami Bigdely

def calc_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def max(li):
    """finds the greatest value in a list"""
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(max(li))

############################
def str_to_array(sentence):
    """takes a string and returns a list"""
    words = sentence[0:].split(' ')
    return words

print(process('If you were a vegetable, you’d be a ‘cute-cumber.'))