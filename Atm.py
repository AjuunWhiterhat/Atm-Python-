class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("Cash has been withdrawn")

    def BalanceEnquiry(self):
        print("Your balance is *****")

machine = Atm(5105105105105100,8068)
print(machine.cardNumber)
print(machine.pinNumber)
print(machine.CashWithdrawl())
print(machine.BalanceEnquiry())
