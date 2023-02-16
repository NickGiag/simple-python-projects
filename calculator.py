
print("Calculator!")
while True:
    option = input("1) Addition \n2) Substraction \n3) Multiplication \n4) Division \n5) Modular forms \nSelect what type of operation you want to calculate: ")
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a second number: "))
    if int(option) == 1:
        sum = number1 + number2
        print("{0} + {1} = {2}".format(number1,number2,sum))
    elif int(option) == 2:   
        sum = number1 - number2 
        print("{0} - {1} = {2}".format(number1,number2,sum))
    elif int(option) == 3:
        sum = number1 * number2  
        print("{0} * {1} = {2}".format(number1,number2,sum))  
    elif int(option) == 4:    
        if number2 == 0:
            print("Can not divide by zero!")
        else:
            sum = number1 / number2
            print("{0} / {1} = {2}".format(number1,number2,sum))
    elif int(option) == 5: 
        sum = number1 % number2  
        print("{0} % {1} = {2}".format(number1,number2,sum)) 

    exit = input("Want to do another calculation? (yes/no)")
    if exit == "no":
        break

