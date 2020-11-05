def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:

    userImp = int(input())

    while True:
        if collatz(userImp) != 1:
            userImp = collatz(userImp)
            print(userImp)
        elif collatz(userImp) == 1:
            print(collatz(userImp))
            break


except:
    ValueError
    print('Please use type an integer!')
