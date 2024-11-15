"""Working With Recursive Functions."""

from __future__ import annotations

__author__ = "730739772"


class Node:
    """OOP for creating linked lists (Nodes)."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes attributes value and next."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # could write self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# print(one)
# print(str(courses))
# print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# print(to_str(one))
# print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the "last" node
    if head.next is None:
        return head.value
    else:
        # Recurvise Case
        rest: int = last(head.next)
        return rest


# print(last(one))
# print(last(courses))


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of the Node at a given index."""
    if head is None:  # Base case for an empty list
        raise IndexError("Index is out of bounds on the list")
    elif index == 0:  # Base case when index is 0
        return head.value
    else:  # Recursive function call
        return value_at(head.next, index - 1)  # index -1 because we move into next node


def max(head: Node | None) -> int:
    """Returns the max value found in the node."""
    if head is None:  # Base case for an empty list
        raise ValueError("Cannot call max with None")
    elif head.next is None:  # Base case for when last node is reached
        return head.value

    rest_max = max(head.next)  # recursive case to call each other node

    if head.value > rest_max:  # compares current node value to max of prev
        return head.value
    else:
        return rest_max


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of nodes with the same values as items."""
    if len(items) == 0:  # Base case for when items is empty
        return None
    else:  # recursive case
        return Node(items[0], linkify(items[1:]))
    # splice subscription notation "[1:]" is inclusive of 1 -> end of list


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list multiplied by the scale factor."""
    if head is None:  # Base case incase empty
        return None
    else:
        head_2 = Node(head.value * factor, scale(head.next, factor))
        # recursive case for head.next
        return head_2
