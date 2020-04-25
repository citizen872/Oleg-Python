i = 0
flag = True
while flag:
    value_1 = int(input("input first number"))
    value_2 = int(input("input second number"))
    command = input("input operation")
    if command == '+':
        print(value_1 + value_2)
    elif command == '-':
        print(value_1 - value_2)
    elif command == '*':
        print(value_1 * value_2)
    elif command == '/':
        print(value_1 / value_2)
    else:
        print( "Wrong command")
        i += 1
        while True:
             command = input ('Continue Y/N')
             if command=='N':
                flag = False
                break
             elif command=='Y':
                break
             else:
                 print("wrong command")
                 i += 1
                 if i == 3:
                     flag = False
                     print("too much errors!!!")
                     break

