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
        for i in range(4):
            while True:
             command = input ('Continue Y/N')
             if command =='Y':
                break
             elif command =='N':
                flag = False
                break
             else:
                 print("wrong command")
                 if i == 2:
                     print("too much errors!!!")
                     flag = False
                     break

