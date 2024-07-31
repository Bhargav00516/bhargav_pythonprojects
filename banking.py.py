
print('='*20)
customerNames = ['pawan', 'ramarao', 'charan', 'mahesh', 'arjun']
customerPins = ['2024', '2029', '2034', '2023', '2049']
customerBalances = [10000, 20000, 20000, 40000, 10000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

while True:
    
    print("*********************************************")
    print("<<<<<ALL INDIA ANDHRA BANK WELCOMES YOU>>>>>")
    print("*********************************************")
    print("PRESS [1] TO Open a new account")
    print("PRESS [2] TO Withdraw Money")
    print("PRESS [3] TO Deposit Money")
    print("PRESS [4] TO Check Customers & Balance")
    print("PRESS [5] TO Exit/Quit")
    print("*********************************************")
   
    choiceNumber = input("SELECT YOUR OPTION")
    if choiceNumber == "1":
        print("YOUR OPTION IS [1] ")
        NOC = eval(input("How many are willing to open"))
        i = i + NOC
        if i > 5:
            print("\n")
            print("LIMIT REACHED")
            print("CONTACT BANK")
            i = i - NOC
        else:
            while counter_1 <= i:
                name = input("Please enter your full name: ")
                customerNames.append(name)
                pin = str(input("SET A PIN : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("ENTER DEPOSIT VALUE: "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is SUCCESSFULLY added to our bank database")
                print("Your pin is added")
                print("Your balance is added")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("thank you---------ALL INDIA ANDHRA...")
                print("==============================TEAM")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("YOUR OPTION [2] ")
        while j < 1:
            k = -1
            name = input("YOUR NAME : ")
            pin = input("YOUR PIN : ")
        while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n") 
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
        if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("YOUR OPTION [3] ")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("PIN : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("YOUR OPTION [4] ")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        print("YOUR OPTION [5]")
        print("Thank you")
        print("VISIT AGAIN")
        print("TEAM")
        print("*****ALL INDIA ANDHRA")
        break
    else:
        print("Invalid option selected by the customer/Something went wrong")
        print("Please Try again!")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")