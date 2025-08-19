# li={1,2,3,4}
# for i in li:
#     print(i,end=',')

# n=int(input('enter a value: '))
# for i in range(1,11):
#     print(f'{n}*{i}={i*n}')

# list1=[101,20,38,55,78,1]
# for i in list1:
#     if i%2==0:
#         print(i,end=',')

#datatype conversions

# num1=int(input('enter num1'))
# num2=int(input('enter num2'))
# print(int(num1) + int(num2))

# num1= 5.5
# print(num1)
# print(int(num1))
# print(num1) 

# num1= 5.5
# num1 = int(num1)
# num1 = float(num1)
# print(num1)

# com=35j
# print(int(com))

# str1 = 'Good Morning'
# print(list(str1))

# print(int('314'))
# print(int('3.



# ----------- problem sloving---------

# age=int(input('Enter the age:'))
# def fun(age):
#     if age>=18:
#         return 'Your aligiable'
#     else:
#         return 'Your not aligiable'
#         print(fun(age))


# a=int(input('Enter the number'))
# b=int(input('Enter the number'))
# c=int(input('Enter the number'))
# def fun(a,b,c):
#     if a>b and a>c:
#         if b>c:
#             section=b
#         else:
#             section=c
#         large=a
#     elif b>a and b>c:
#         large=b
#         if a>c:
#             section=a
#         else:
#             section=c
#     else:
#         if b>a:
#             section=b
#         else:
#             section=a
#         large=c
#     return large+section

# print(fun(a,b,c))



# s=input()
# res=""
# for i in range(len(s),-1,-1,-1):
#     res+=s[i]
# if res==s:
#     print('Yes')
# else:
#     print('No')





# A=int(input())
# c=A
# w=A 
# while W>=3:
#     E=w//3
#     c+=E
#     w=E + w%3
# print(c)



# def check_even_odd(num1):
#     if num1 % 2 == 0:
#         return True
#     else:
#         return False


# def check_even_odd(num1):
#     if num1 % 2 == 0:
#         return True
#         return False


# def check_even_odd(num1):
#     return True if num1 % 2 == 0 else False


# num1 = int(input('Enter the first number'))
# num2 = int(input('Enter the second number'))
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# print(num1) if num1 > num2 else print(num2)

# num1 = int(input('Enter the number'))
# num2 = int(input('Enter the number'))
# def greatest(num1,num2):
#     return (num1 if num1 > num2 else 'both are equal' if num1 == num2 else num2)
# print(greatest(num1,num2))

# num1 = int(input('Enter the first number'))
# num2 = int(input('Enter the second number'))
# op = input('Enter the operators ') # .lower()add
# def simple_cal(num1,num2,op):
#     if op == '+'or op == 'add': #if op in ['+','add','Add']:
#         return num1 + num2          
#     elif op == '-':
#         return num1 - num2
#     elif op == '*':
#         return num1 * num2
#     elif op == '/':
#         return num1 / num2 if num2 != 0 else 'Invalid denominator'
#     else:
#         return 'Invalid operator'

# res = simple_cal(num1,num2,op)
# print(res)


# num1 = 5
# num2 = 7
# num3 = 9
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num3:
#     print(num2)
# else:
#     print(num3)



# year = 1700

# if year % 400 == 0:
#     print('Leap year')
# elif year % 100 != 0 and year % 4 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')

#          (0r)

# if year % 400 == 0 or  year % 100 != 0 and year % 4 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')



# if marks > 90:
#     print('A')
# elif marks > 80:


# s1 , s2 , s3 = 2, 9 , 5
# if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
#     print('Triangle can be formed')
# else:
#     print('Triangle not can be formed')

# (s1)**2 == (s2)**2 + (s3)**2 or (s2)**



# input_char = input('Enter a character').lower()

# def check_char(input_char):
#     if len(input_char) != 1:
#         return 'Invalid input'

# if input_char in ['a' , 'e' , 'i' , 'o' , 'u']:
#     print('Vowels')
# elif input_char.isalpha():
#     print('Consonant')
# else:
#     print('Neither')


num1 = int(input('Enter a number :'))
num2 = int(input('Enter a number :'))
num3 = int(input('Enter a number :'))
def check_triangle(num1 , num2 , num3):
    if num1 + num2 > num3 and num2 + num3 > num1 and num3 + num1 > num2:
        print('Its can formm a triangle')
        if num1 == num2 == num3:
            print('It is  a equilateral traingle')
        elif num1 == num2 or num2 == num3 or num2 == num1:
            print('It is a isosceles triangle')
        else:
            print('It is a scalence traingle')
        if (num1**2 + num2**2 == num3**2) or (num2**2 + num3**2 == num1**2) or (num3**2 + num1**2 == num2**2):
           print('It is a right angle triangle')
        else:
          print('It is not right angle triangle')
    else:
         print('It can form a triangle')

check_triangle(num1,num2,num3)




        
