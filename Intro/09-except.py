try:
    number1 = int(input('Input number one: '))
    number2 = int(input('Input number two: '))

    number = number1 / number2
    print('You number: ', number)
except ValueError as e:
    print('Not valid data: ', e)
except ZeroDivisionError as e:
    print('Not zero number2: ', e)
except Exception:
    print('Error')


print('The end')
