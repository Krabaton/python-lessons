inp = int(input('Input var: '))

if inp > 5:
    print('Yes')
elif inp is 0:
    print('0')
else:
    print('No')

temp = 'Yes' if inp < 0 else 'No'

print(temp)