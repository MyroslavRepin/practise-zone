class Bank:
    USERS = []

    def __init__(self, username) -> None:
        self.balance = 0
        self.username = username
        Bank.USERS.append(self.username)

    def deposit(self, add_funds):
        self.balance += add_funds
        return f'{add_funds} Succesfully deposited'

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return "Not enough funds"
        if withdraw <= self.balance:
            self.balance -= withdraw
            return f'Succesfully sent {withdraw}'

    def get_balance(self):
        return f'Balance: {self.balance}'

    def transfer(self, destination, amount):
        if destination in self.USERS:
            for user in self.USERS:
                if user == destination:
                    return f'Found user: {user}'
                else:
                    'Did not found'
        else:
            return "No such user"


user_1 = Bank(username='myroslav')
user_2 = Bank('artem')
print(user_1.deposit(147))
print(user_1.deposit(50))
print(user_1.withdraw(10))
print(user_1.get_balance())
print(user_1.transfer('artem', 10))
