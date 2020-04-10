int_list = [1, 2, 3]
mix_list = ['str', 0.1, 2, True]
print(len(mix_list))

x = list(range(10))
x[0] = -1
print(x)
print(x[-2])
print(x[:3])
print(x[3:])
print(x[1:5])
print(x[-3:])
print(x[1:-1])
print(x[:])

print(1 in x)
print(0 in x)

y = [1, 2, 3]
a, b, c = y

y.extend([4, 5])
y.append(11)
print(x + y)

my_list = [list1 for list1 in 'Hello world']
print(my_list)
my_list.insert(3, '!')
print(my_list)
a = my_list.pop(0)
print(my_list)
# my_list.remove('t')
my_list.clear()

for _, val in enumerate(int_list):
    print(val)
