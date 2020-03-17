how_high = int(input("How high should I go? "))
first = 0
second = 1
print(first)
print(second)
while (first + second < how_high):
    next_number = first + second
    print(next_number)
    first = second
    second = next_number