import time
print("Please insert your card")

time.sleep(2)

password = 1235

balance = 100000

pin = int(input("Enter your 4 digit pin:"))

if pin == password :
    print("\t\t\t\t WELCOME TO SBI ")
    print("Choose Your Method:-")
    print('''  
              1 - BALANCE ENQUIRY
             
              2 - WITHDRAW
          
              3 - PIN GENARATE
            
              4 - QUIT
          
               ''' )
    ch = input("Your Method: ")
           
    if ch == '1' :
        print("\t\t\t\t YOUR BALANCE ")
        print(balance)
        
    if ch == '2' :
        print("\t\t\t\t CHOOSE YOUR WITHDRAW METHOD ")

        print(''' 
                  1 -  SAVINGS
              
                  2 - CURRENT
              
                   ''')
        m = input("Your Method: ")
        m.lower
        if m == '1' :
            amt = int(input("Enter Amount: "))
            if (amt <= balance):
                print("Your Withdraw Is Succesfull")
                amt -= balance
            elif (amt>balance):
                print("Your Amount Exceeding Your Balance!!!")
        elif m == '2' :
            amt = int(input("Enter Amount: "))
            dep = amt - balance
    if ch == '3' :
        npin = int(input("Enter Your previous Pin: "))
        if npin == password :
            password = int(input("Enter New Password: "))
            print("YOUR PIN CHANGED SUCCESSFULLY")
    if ch == '4' :
        exit(0)

else :


    print("   Wrong pin")
    print("   TRY AGAIN")
print("\t\t\t\t THANK YOU ")