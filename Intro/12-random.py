import random

four_random = [random.random() for _ in range(4)]

print(four_random)

print(random.randrange(10))
# random.seed(3)
print(random.randrange(3, 11))

my_list = list(range(10))
print(my_list)
random.shuffle(my_list)
print(my_list)

random.choice(['Alica', 'Cat', 'Hat'])

my_numbers = range(20)

win_numbers = random.sample(my_numbers, 3)
print(win_numbers)