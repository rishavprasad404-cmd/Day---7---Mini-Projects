print("============== ATM System =========================")
passw = input("Set a Password = ")
total_balance = float(input("Enter your Total Balance = "))
pass_again = input("Enter your Password Again ? = ")
if passw == pass_again :
    print("Welcome Access Granted ! ")
    d = input("Deposit or Withdraw = ")
    if d == "Deposit":
        deposi =  float(input("Enter your Deposited Amount = "))
        d = deposi + total_balance
        print("Deposit Successfully !")
        print("Updated Balance = ",d)
        print("Thank You for Your Transition ! ")
    else:
        withdra = float(input("Enter your Withdraw Amount = "))
        if withdra > total_balance :
            print("Insufficient Balance")
        else:
            d = total_balance - withdra
            print("Withdraw Successfully !")
            print("Updated Balance = ",d)
            print("Thank You for Your Transition !")
else:
    print("Wrong Password")