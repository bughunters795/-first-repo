class Bank:

    def __init__(self,owner,balance,pin):
                        self.owner = owner
                        self.balance = balance
                        self._pin     = pin

    def pin_verfication(self ,pin):
        return pin == self._pin


    def deposit(self,amount,pin):
        if(self.pin_verfication(pin)):
            print('your are allowed for transaction')
            self.balance = self.balance + amount
            print(f'the amount you deposit is {amount}rs')
        else:
            print('your are not allowed for transaction')
        


    def withdraw(self,amount,pin):
        if(self.pin_verfication(pin)):
            print('your are allowed for transaction')
            self.balance =  self.balance - amount
            print(f'the amount you withdraw is {amount}rs')
        else:
               print('your are not allowed for transaction:')

    def showBalance(self,pin):

        if(self.pin_verfication(pin)):
               print('your are allowed to show balance ')
               print(f'{self.owner} your balance is {self.balance}$$')
        else:
               print('your are not allowed to show balance ')
        
        # return a
    


user1 = Bank('usman' , 200 , 1122)
user1.showBalance(1122)
user1.deposit(20,1122)
user1.withdraw(2,1122)
user1.showBalance(1122)