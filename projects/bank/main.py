import json
from datetime import datetime


class Bank:
    USERS = {}
    counter = 1

    def __init__(self, username) -> None:
        self.balance = 0
        self.username = username
        self.varname = f"user{Bank.counter}"
        Bank.USERS[self.username] = self
        Bank.counter += 1

    def loq_history(self, action, amount, to=None):
        FILE_PATH = '/Users/veniaminrepin/Documents/myroslav_repin/projects/practise-zone/projects/bank/loq_history.json'
        loq_dict = {
            'user': self.username,
            'action': action,
            'amount': amount,
            'currency': 'USD',
            'time': datetime.now().isoformat()
        }
        if to is not None:
            loq_dict['to'] = to
        try:
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(loq_dict)
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def deposit(self, add_funds):
        self.balance += add_funds
        self.loq_history("deposit", add_funds)
        return f'{add_funds} Succesfully deposited'

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return "Not enough funds"
        if withdraw <= self.balance:
            self.balance -= withdraw
            self.loq_history('withdraw', withdraw)
            return f'Succesfully withdrawed: {withdraw}'

    def get_balance(self):
        return f'{self.username}\'s Balance: {self.balance}'

    def transfer(self, destination, amount):
        if destination in Bank.USERS:
            user = Bank.USERS[destination]
            print(f'Found user: {destination}')
            # checking if sender has enough money
            if amount <= self.balance:
                self.balance -= amount
                user.balance += amount
                self.loq_history('transfer', amount, destination)
                return f'money sent to: {destination}'
            else:
                return 'not enough money'
        else:
            return "No such user"


user_1 = Bank(username='myroslav')
user_2 = Bank('ben')

print(user_1.deposit(100))
print(user_1.withdraw(50))
print(user_1.transfer('ben', 10))
print(user_1.get_balance() + "\n")

print(user_2.deposit(500))
print(user_2.withdraw(100))
print(user_2.transfer('myroslav', 100))
print(user_2.get_balance())
