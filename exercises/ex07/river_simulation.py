"""Imports river file and simulates life cycle in a river."""

from exercises.ex07.river import River

my_river = River(num_fish=10, num_bears=2)

my_river.view_river()

print(my_river.view_river)

my_river.one_river_week()

print(my_river.view_river())
