"""Calculates distance between two circles"""
# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

# C == Circle
C1_X = 4
C1_Y = 4.25
C2_X = 53
C2_Y = -5.35

# Calculate the distance between the two circle
DIST_X = (C1_X - C2_X)**2
DIST_Y = (C1_Y - C2_Y)**2
TOTAL_DIST = math.sqrt(DIST_X + DIST_Y)

# Prints distance
print('distance', TOTAL_DIST)

#****************************************
"""Calculates length between two vectors"""
# V == Vector
VA_X = -36
VA_Y = 97
VB_X = 0.34
VB_Y = 0.91

# Calculate the length of vector AB (which is between vectors A and B).
LENGTH_X = (VA_X - VB_X) * (VA_X - VB_X)
LENGTH_Y = (VA_Y - VB_Y) * (VA_Y - VB_Y)
TOTAL_LENGTH = math.sqrt(LENGTH_X + LENGTH_Y)

# prints distance
print('length', TOTAL_LENGTH)
