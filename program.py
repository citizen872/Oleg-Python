flag = True
j = 0
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
        j+=1
        for i in range(3):
            if j==3:
                print("to much errors!!!")
                flag = False
                break
            command = input ('Continue Yes/No')
            if command=='Yes':
                command = input("input operation")
                if command == '+':
                    print(value_1 + value_2)
                    break
                elif command == '-':
                    print(value_1 - value_2)
                    break
                elif command == '*':
                    print(value_1 * value_2)
                    break
                elif command == '/':
                    print(value_1 / value_2)
                    break
                else:
                    print("Wrong command")
                    j += 1
            elif command=='No':
                flag = False
                break
            else:
                 print("wrong command")
            if i == 2:
                  flag = False
                  print("too much errors!!!")
                  break
    command = input('Continue Yes/No')
    if command == 'Yes':
        continue
    elif command == 'No':
        print("Goodbye")
        flag = False
        break
    else:
        print("Wrong command")
        flag= False