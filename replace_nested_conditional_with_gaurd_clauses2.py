"""Replace nested conditional with guard classes."""
# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

class idk:
    def __init__(self, *args, **kwargs):
        self.adj_factor = 0.7

    def conditional(self):
        """greater than zero"""
        if (capital > 0):
            if (rate > 0):
                if (duration > 0):
                    return True
        return False

    def get_adjusted_capital(self, capital, rate, duration, income):
        result = 0
        if self.conditional():
            return (income / duration) * self.adj_factor

adjusted_capital = idk.get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)
