# 9. ООП: Name mangling
from datetime import datetime, date
import pytz


WHITE = '\u001b[37m'
GREEN = "\033[0;92m"
RED = "\033[1;31m"

class Account:  
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'Вы потратили {amount}')
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])    
        else:
            print('Не достаточно денег')
            self.show_balance()

    def show_balance(self):
        print(f'Ваш баланс: {self.__balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'зачисление'
                color = GREEN
            else:
                transaction = 'снятие средств'        
                color = RED
            print(f'{color} {amount} {WHITE}{transaction} в {date.astimezone()}')    

a = Account("Алексей", 1000)

a.__balance = 100000000
print(a.__dict__) 
# {'name': 'Алексей', '_Account__balance': 100000000, '_history': []}