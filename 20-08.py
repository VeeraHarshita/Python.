# while True:
#     print('1. addition 2. substaction 3. multiplication 4. division')
#     choice = input('Enter your number :')
#     if choice == '1' or choice == 'addition':
#         input_num1 = float(input('Enter the number: '))
#         input_num2 = float(input('Enter a number: '))
#         print(input_num1 + input_num2)

#     elif choice == '2' or choice == 'substraction':
#         input_num1 = float(input('Enter the number: '))
#         input_num2 = float(input('Enter a number :'))
#         print(input_num1 - input_num2)

#     elif choice == '3' or choice == 'multiplication':
#          input_num1 = float(input('Enter the number: '))
#          input_num2 = float(input('Enter a number :'))
#          print(input_num1 * input_num2)

#     elif choice == '4' or choice == 'division':
#          input_num1 = float(input('Enter the number: '))
#          input_num2 = float(input('Enter a number :'))
#          print(input_num1 / input_num2)


#     else:
#         print('No valid option picked')
#         print('Exiting')
#         break
        

      # 1 to 100 divisiable by 3 and 5 using loop
# def table(n):
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print(f'{n} x {i} = {n*i}')
# table(3 and 5)


# factirial using while loop

# n=int(input('Enter a number :' ))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print('Factional of {n} is : {fact}')


# login system

correct_password = '123456'
attempts = 3
while attempts:
    password = input('Enter password :')
    if password == correct_password:
        print('Login successful')
        break
    attempts -= 1
if attempts == 0:
    print('Account locked')


