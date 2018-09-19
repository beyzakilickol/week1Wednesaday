
number = int(input('Enter your number: '))
#result = 1
def pos_num():
    result = 1
    for i in range(1, number + 1 , 1):
        result = result * i
        if(number == 0):
            print(1)
    print(result)
def factorial():
    if(number < 0):
        print('it does not have a factorial')
    else:
        return pos_num()
factorial()



#ositive_numbers = pos_num()


#    else:
#        return positive_numbers






#------------gives error below-------------------------------
#def factorialOfNumber(n):
    #if(n > 1):
    #    return n * factorialOfNumber(n - 1)
#    elif(n == 0):
#        return 1
#    else:
#        return 1 ??????????????????????

#if(number < 0):
#    print("No factorial")
#else:
#    calculate_factorial()
