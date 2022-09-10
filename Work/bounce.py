# bounce.py
#
# Exercise 1.5

height = 100
bounce_count = 0
while bounce_count < 10:
    bounce_count += 1
    height *= (3/5)
    print(bounce_count, round(height, 4))
