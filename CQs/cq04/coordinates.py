"""Gathering formatted pairs of each character in the two strings"""

__author__ = "730739772"


def get_coords(xs: str, ys: str) -> None:

    x_idx = 0  # set index to 0 before initial while loop

    while x_idx < len(xs):  # characters in xs
        y_idx = 0  # set index to 0 before going into nested while loop
        while y_idx < len(ys):  # characters in ys
            print("(" + xs[x_idx] + "," + ys[y_idx] + ")")
            y_idx += 1  # increase ys index in nested loop
        x_idx += 1  # increase xs index by 1 out of nested while loop
