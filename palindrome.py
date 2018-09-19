word = input('Enter the word: ')
arr = list(word)

second_word = []
for index in range(len(arr)-1, -1 , -1):
    second_word.append(arr[index])


print(second_word)
reversed = ''.join(second_word)
print(reversed)

def is_palindrome():
    if(word == reversed):
        return True
    else:
        return False

print(is_palindrome())
#-----------------------------------second way-----------------------
#word = input('Enter the word: ')
#reversed = word[::-1]
#def is_palindrome():
#    if(word == reversed):
#        return True
#    else:
#        return False

#print(is_palindrome())
