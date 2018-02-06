import time
count = 0
gap = print ("\n")
instances = []
def openAccount:
    print ("You are about to open an account with Ca$hCa$h MoneyMoney Inc")
    count = Customer()
    (count).name = input ("What is your company name?")
    (count).password = input ("please set a password")
    instances.append(count.name)
    count + 1
    print ("please log in now")
    print (gap * 10)

def closeAccount:
    Cname = input ("What is your company name?")
    Cpass.password = input ("please enter a password")
    if Cname.password == Cpass:
        instances.remove(Cname)
        del (Cname)
        print ("Your account has now been deleted. \n It is ", time.strftime("%c"))
    print ("Have a nice day")
    print (gap * 10)


class Customer(object):

    def __init__(self, name, password, balance=0.0):
        self.name = name
        self.balance = balance
        self.password = password

    def withdraw(self, amount):
        if amount > self.balance:
            print("You do not have enough money in your account.")
            break
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
     
while True:
yORn = input ("Good morning, do you have an account with us?")
    if yORn == "yes"
        login()
        break
    elif  yORn == "no"
        openAccount()
        break
    else
         print ("yes or no please")
def login:
    print ("What is your account name?")
    logName = input ("")
    print ("What is your password?")
    logPass = input ("")
    if logName.password == logPass:
        print ("Welcome ", logName, "you have successfully logged in.")
        print ("Today is ", time.strftime("%c"))
print ("Would you like to: \nA) Make a withdrawl \nB) Make a deposit \nC) Logout")
an = input ("")
while true
