i = 10
# print(i==10) # == means check if left is same as right
# print(1!=10) #
# print(i<20) #
# print(i>20) # >, <, >=, <=, ==, !=
# print(i>20 and i <30)
# print(i<20 and i> 5)
# print(i<20 or i>5)
# print(i<20 or i<5)

# str = "Fred"
# print(str=="Tom")
# print(str!="Tom")
# print(str=="Fred") #True
# print(str=="Fred ") #False
# print(str=="fred") #False

# String Functions
# word1 = 'HelloFromFred'
# print(word1.isalpha()) # is alpha == checking if ONLY LETTERS
# word2 = '7890'
# print(word2.isalnum()) # is alpha == checking if ONLY NUMBERS

# word1 = "Hello"
# word2 = 'HELLO'
# word3 = "hello"
# print('Check if all 3 variables are uppercase,')
# print(word1.isupper())
# print(word2.isupper())
# print(word3.isupper())

# word1 = "Hello"
# word2 = 'HELLO'
# word3 = "hello"
# # print('Check if all 3 variables are lowercase,')
# # print(word1.islower())
# # print(word2.islower())
# # print(word3.islower())
#
# print('check if string starts with a pattern of characters')
# print(word1.startswith('He'))
# print(word2.startswith('He'))

#---------- If statements-------
# num = 9
# print(type(num))
# if num==10: #
#     print('Yup it is 10')
#
# if num==10: print('Yup it is 10 too')
#

# if ... else ... statement
# entry = input("Please type in an integer here: ")    #input treated as string
# num = int(entry)    # convert variable from type string to type int
# if num==10:
#     print('Yup it is 10')
# else:
#     print('Nope it is not 10')

# if ... elif... elif... else(optional)
# entry = input("Please type in an integer here: ")    #input treated as string
# num = int(entry)    # convert variable from type string to type int
# if num==10:
#     print('Yup it is 10')
# elif num >10:
#     print('Nope it is > 10')
# else:
#     print('It is <10')


# Another example
# entry = input('Please type an integer here: ')
# num = int(entry)
#
# if num>=10:
#     print('The number you entered is >= 10')
# elif num >0 and num <10:
#     print('The number you entered is between 0 and 10')
# elif num<0:
#     print('The number you entered is <0')

# More complex example
# color = input('What color is your car? ')
# year = int(input('What year is your car? '))
#
# if (color=='red' and year<1978) or (color=='blue' and year < 1965):
#     print('You have a classic sports car! \n new line!')
# else:
#     print('you car is a lot newer and nicer')

# age = 39
# ticket = 'child' if age <= 13 else 'adult'
# print(ticket)
#
# # a more comprehensive way
# age = 39
# ticket = ''
# if age < 13:
#     ticket = 'child'
# else:
#     ticket = 'adult'
# print(ticket)


# Loops
# Basic loop, goes from 0 to 9
# for i in range(10):
#     print(i)
#
# for i in range(5,10,2):
#     print(i)


# for loop syntax:
# for i in some_list:
# Do something


# nested for loop
# for x in range(0,5,1): #x =0,1,2,3,4
#     for y in range(1,4,2): #y = 1,3
#         for z in range(2,5,2):
#         print(x,y,z)


# while statement
# i = 1
# while i<10:
#     print(i)
#     i += 1
#
# print('after while loop:')
# print(i)

# how to break out for loop
# for x in range(10):
#     print(x)
#     entry=input('Would you like to continue? (Y/N)')
#     if (entry=='N'):
#         break
#

num = int(input('What is your favorite positve ineger number?'))
if num < 1:
    print('Sorry you are dumb')
else:
    while (num>0):
        print(num)
        entry = input('Would you like to continue? (y/n)')
        if entry == 'n':
            break
        num = num - 1




