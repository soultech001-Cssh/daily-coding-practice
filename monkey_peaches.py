# Monkey Eating Peaches Problem
# A monkey picks peaches on day 1. Each day it eats half plus one more.
# On day 10, only 1 peach remains. Find how many peaches were picked on day 1.

# Start with 1 peach on day 10
peaches = 1

# Iterate backwards from day 9 to day 1
for day in range(9, 0, -1):
    peaches = (peaches + 1) * 2

# Print the result (ensuring it's an integer)
print(int(peaches))
