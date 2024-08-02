while True:
    print("addition")
    print("subtraction")
    print("multiplication")
    print("division")
    print("floor division")
    print("exponent")

    choice= input("enter choice=")
    if choice in ('1','2','3','4','5','6','7'):
        num1 = int(input('enter thhe first'))
        num2 = int(input('enter the second number'))

    if choice == '1':
        print('addition',(num1+ num2))
    elif choice =='2':
        print('subtraction',(num1-num2))
    elif choice =='3':
        print('multiplication',(num1*num2))  
    elif choice == '4':
        if num2 !=0:        
           print('Division: ',(num1/num2))
        else:
            print('Divided by zero!')
    elif choice == '5':
        print('Floor Division: ',(num1//num2)) 
    elif choice == '6':
            print('Power: ',(num1**num2))
    elif choice == '7':
        break
    else:
        print('Invalid Input')  