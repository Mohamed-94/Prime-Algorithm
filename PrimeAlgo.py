for number in range(10,100000):
    for x in range(2,number):
        if number % x == 0:
            j = number / x
            print("%d equals %d * %d" % (number,x,j))
            break
        else:
            print(number,"is prime number")
