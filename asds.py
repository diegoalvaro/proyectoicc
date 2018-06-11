num =int(input('digite numero:'))
factorial=1


def factorial(num):
    for i in range(num):
        factorial=(factorial*num)
        num=num-1

re=factorial(num)
print(re)
