"""This module prints students statistics"""
# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

class StudentStatistics():
    """Class that runs all our statistics"""
    def __init__(self):
        self.grade_list = []
        self.total = 0
        self.mean = 0

    def s_d(self):
        """Calculates standard deviation of the grades"""
        sum_of_squares = 0
        for grade in self.grade_list:
            sum_of_squares += (grade - self.mean) ** 2
        return math.sqrt(sum_of_squares / len(self.grade_list))

    def get_mean(self):
        """Calculates mean and total of the grades"""
        for grade in self.grade_list:
            self.total = self.total + grade
        self.mean = self.total / len(self.grade_list)

    def get_input(self):
        """Collects and returns input for n students aka grade_list"""
        n_student = 5
        for _ in range(0, n_student):
            self.grade_list.append(int(input('Enter a number: ')))

    def print_stat(self):
        """prints out statistics of n_students grades"""
        # Get the statistics
        self.get_input()
        self.get_mean()
        mean = self.mean
        s_d = self.s_d()
        # print out the mean and standard deviation in a nice format.
        print('****** Grade Statistics ******')
        print("The grades's mean is:", mean)
        print('The population standard deviation of grades is: ', round(s_d, 3))
        print('****** END ******')

s = StudentStatistics()
s.print_stat()
