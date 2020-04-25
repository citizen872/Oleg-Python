i = 0
flag = True
while flag:
    value_1 = int(input("input first number"))
    value_2 = int(input("input second number"))
    command = input("input operation")
    if command == '+':
        print(value_1 + value_2)
        while True:
             command = input ('Continue Yes/No')
             if command=='Yes':
                break
             elif command=='No':
                flag = False
                break
             else:
                print("wrong command")
                i += 1
                if i == 3:
                    flag = False
                    print("too much errors!!!")
                    break
    elif command == '-':
        print(value_1 - value_2)
        while True:
             command = input ('Continue Yes/No')
             if command=='Yes':
                break
             elif command=='No':
                flag = False
                break
             else:
                 print("wrong command")
                 i += 1
                 if i == 3:
                     flag = False
                     print("too much errors!!!")
                     break
    elif command == '*':
        print(value_1 * value_2)
        while True:
             command = input ('Continue Yes/No')
             if command=='Yes':
                break
             elif command=='No':
                flag = False
                break
             else:
                 print("wrong command")
                 i += 1
                 if i == 3:
                     flag = False
                     print("too much errors!!!")
                     break
    elif command == '/':
        print(value_1 / value_2)
        while True:
             command = input ('Continue Yes/No')
             if command=='Yes':
                break
             elif command=='No':
                flag = False
                break
             else:
                 print("wrong command")
                 i += 1
                 if i == 3:
                     flag = False
                     print("too much errors!!!")
                     break
    else:
        print( "Wrong command")
        while True:
             command = input ('Continue Yes/No')
             if command=='Yes':
                break
             elif command=='No':
                flag = False
                break
             else:
                 print("wrong command")
                 i += 1
                 if i == 3:
                     flag = False
                     print("too much errors!!!")
                     break