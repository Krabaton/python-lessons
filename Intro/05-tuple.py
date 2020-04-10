my_tuple = (1, 2)
other_tuple = 2, 3

try:
    my_tuple[0] = 3
except TypeError:
    print('Tuple immutable!')


def sum_and_mul(x, y):
    return (x + y), (x * y)


print(sum_and_mul(2, 3))

x = 2
y = 3

x, y = y, x
print(x, y)

list_student = ['Darya', 'Maksim', 'Vasya']

students = tuple(list_student)
print(students)
for i in students:
    print(i)