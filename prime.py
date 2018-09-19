number = int(input('Enter your number: '))

#def consonant(s):
#    for n in range(2, s, 1):
#        if number % n == 0:
#            print('Not a prime')
#            break
#        else:
#            print('Prime')
#            break


#consonant(number)
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n, 1):
        if n % i == 0:
            return False

    return True

print(isPrime(number))
