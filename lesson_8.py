# 8. ООП: Пример 1
from datetime import datetime, date
import pytz


WHITE = '\u001b[37m'
GREEN = "\033[0;92m"
RED = "\033[1;31m"

class Account:  
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Вы потратили {amount}')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])    
        else:
            print('Не достаточно денег')
            self.show_balance()

    def show_balance(self):
        print(f'Ваш баланс: {self.balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'зачисление'
                color = GREEN
            else:
                transaction = 'снятие средств'        
                color = RED
            print(f'{color} {amount} {WHITE}{transaction} в {date.astimezone()}')    

a = Account("Алексей", 1000)

a.deposit(100)

a.withdraw(550)

a.deposit(2777)

a.show_history()