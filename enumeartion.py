from enum import Enum

class colors(Enum):
    red = 1
    green = 2
    blue = 3

lister = [x for x in colors]

print(colors.red)
print(colors(2))
print(colors['blue'])
print(lister)