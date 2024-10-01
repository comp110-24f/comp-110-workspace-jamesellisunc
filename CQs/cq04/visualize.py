"""Imports functions from concatenation and coordinates modules"""

__author__ = "730739772"

# importing function from concatenation module
from CQs.cq04.concatenation import concat

# importing function from coordinates module
from CQs.cq04.coordinates import get_coords

# Global variables
x = "123"
y = "abc"

print(concat(x, y))  # positional arguments

get_coords(x, y)
