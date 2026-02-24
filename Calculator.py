print ("welcome to the calculator. Innput two positive values in when asked and and operation +,-,/, or *")
name = input("Enter your name: ")
print("Hello! Let's get started", name)
try:
            num1 = input("Enter your first number: ")
            num1= int(num1)

            if num1 < 0 :
                print("⚠ Invalid Number. Please input a positive number")
            num2 = input("Enter your Second number: ")
            num2= int(num2)

            if num2 < 0 :
                print("⚠ Invalid Number. Please input a positive number")
            operation = input("Enter your operation, +,-,/, or *(use double asterisks to square a base by its exponent): ")
            if operation==("+"):
                print(num1+num2)
            elif operation==("-"):
                print(num1-num2)
            elif operation==("*"):
                print(num1*num2)
            elif operation==("/"):
                if num2==0:
                    print("The second number cannot be divisible by 0. Use a different number")
                else:
                    print(num1/num2)
            elif operation==("**"):
                print(num1**num2)
            else:
                print("⚠ Invalid input. Please enter a valid operation.")

except ValueError:
            print("⚠ Invalid input. Please enter a valid number.")
            
                        

   
