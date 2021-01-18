class Atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def checkBalance(self):
        print ('Yourre Balance is 50,000 Rs')
    def withdrawal(self, amount):
        new_amount = 50000 - amount
        print ('remaining balance is' + str(new_amount))
def main():
    cardNumber = input('enter your cardNumber')
    pin =  input('Enter Your Pin')
    user = Atm(cardNumber,pin)
    print ('Choose your activity')
    print ('1. Balance Enquiry 2. Withdrawal')
    activity = int(input('Enter your Activity'))
    if activity == 1 :
        user.checkBalance()
    elif activity == 2 :
        amount = int(input('Enter The Amount'))
        user.withdrawal(amount)
    else:
        print ('Enter a Valid Number')
main()
