print("WELCOME TO THE BANK\nPLEASE ENTER YOUR CARD \nCARD ENTERED SUCCESSFULLY")

def register():
    db=open("database.txt","r")
    Username=input("Create Your Username: ")
    password=input("Create PIN: ")
    while (password.isnumeric()==False or len(str(password))!=4):
        print("PIN should be numeric and PIN should be of four digit.Try Again!!")
        print('\n================================================================\n==================================================')
        password=(input("Create PIN: "))
        
    
       
    password1=(input("Confirm PIN:"))
    d=[]
    f=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))
        

    if password != password1:
        print("PINs dont match please restart")
        print('\n================================================================\n==================================================')
        register()
    else:
        pass
    if Username in d:
           print('Username Exist')
           print('\n================================================================\n==================================================')
           register()
    else:
            db=open('database.txt',"a")
            db.write(Username+", " + str(password) + '\n')
            print('Successfully created an account with initial balance of Rs 50000!\nNow login.')
            print('\n================================================================\n==================================================')
            db.close()
            home()


def access():
    db=open("database.txt","r")
    Username=input("Enter Your Username: ")
    Password=(input("Enter Your PIN: "))

    if not len(Username or Password)<1:
        d=[]
        f=[]
        for i in db:
            a, b=i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b)
            data=dict(zip(d,f))
        
        try:
            if data[Username]:
                try:
                    if Password==data[Username]:
                        print("Login Successful!")
                        print('\n================================================================\n==================================================')
                        print("Hi" ,Username, "Welcome to your account!\n")
                        account.option(user)
                        
                    else:
                        print("Username or Password Incorrect\nLogin Again.")
                        print('\n================================================================\n==================================================')
                        access()
                except:
                    print("Incorrect Password or Username\nLogin Again.")  
                    print('\n================================================================\n==================================================')    
                    access()
            else:
                print("Username or Password Does not Exist.")
                print('\n================================================================\n==================================================')
                access()
                
        except:
            print("Username or Password does not Exist")  
            print('\n================================================================\n==================================================')
            access()
            
class user:
    balance=50000
    acc_balance = balance

        



class account(user):
    
    
    
    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
            print('\n================================================================\n==================================================')
        else:
            print('Invalid amount transaction aborted')
            print('\n================================================================\n==================================================')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
            print('\n================================================================\n==================================================')
        else:
            print('Invalid amount transaction aborted')
            print('\n================================================================\n==================================================')
    def balance(self):
        print("You have an account balance of : ₹" ,self.acc_balance)
        print('\n================================================================\n==================================================')

    def option(self):
        enter=int(input("\n(1)Deposit \n(2)Withdraw \n(3)balance \n(4)Exit\n Choose an option : "))
        if enter==1:
            account.deposit(self)
            account.option(self)
        elif enter==2:
            account.withdrawl(self)
            account.option(self)
        elif enter==3:
            account.balance(self)
            account.option(self)
        elif enter==4:
            home()

            

        else:
            account.option(user) 
            


def home (option=None):
    option=int(input("(1)Login \n(2)Signup\nEnter an option : "))
    if option==1:
        access() 
        
        
        
    elif option == 2:
        register()

    else:
        print("Enter an option!!")
        home()
home()


    
