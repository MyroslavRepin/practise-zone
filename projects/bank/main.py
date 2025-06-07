class Bank:
    USERS = {}
    counter = 1

    def __init__(self, username) -> None:
        self.balance = 0
        self.username = username
        self.varname = f"user{Bank.counter}"
        Bank.USERS[self.username] = self.varname
        Bank.counter += 1

    def deposit(self, add_funds):
        self.balance += add_funds
        return f'{add_funds} Succesfully deposited'

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return "Not enough funds"
        if withdraw <= self.balance:
            self.balance -= withdraw
            return f'Succesfully withdrawed {withdraw}'

    def get_balance(self):
        return f'Balance: {self.balance}'

    def transfer(self, destination, amount):
        if destination in Bank.USERS:
            user = Bank.USERS[destination]
            print(f'Found user: {user}')
            # checking if sender has enough money
            if amount <= self.balance:
                self.balance -= amount
                # TODO: make a transfer
                # user = Bank.USERS[destination]
                # user.balance += amount
                return 'money sent'
            else:
                return 'not enough money'
        else:
            return "No such user"


user_1 = Bank(username='myroslav')
user_2 = Bank('artem')
user_3 = Bank('ben')
print(user_1.deposit(add_funds=100))
print(user_1.get_balance())
print(user_1.transfer('ben', 10))
