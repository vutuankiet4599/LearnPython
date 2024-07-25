class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self._balance = 0.0

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self._balance += amount

    def withdraw(self, amount, description=''):
        if self._balance < amount:
            return False
        
        self.ledger.append({
            'amount': 0 - amount,
            'description': description
        })
        self._balance -= amount
        return True

    def get_balance(self):
        return self._balance

    def transfer(self, amount, budget):
        from_message = f'Transfer from {self.name}'
        to_message = f'Transfer to {budget.name}'

        if self._balance < amount:
            return False
        
        self.ledger.append({
            'amount': 0 - amount,
            'description': to_message
        })
        self._balance -= amount
        budget.deposit(amount, from_message)

        return True
    
    def check_funds(self, amount):
        return amount <= self._balance
        
    def __str__(self):
        result = ''

        result += self.name.center(30, '*')
        result += '\n'

        for item in self.ledger:
            description = item['description']
            if len(description) > 23:
                description = description[:23]
            description_len = len(description)
            amount = f'{item["amount"]:.2f}'
            amount_len = len(amount)

            result += description
            result += ' ' * (30 - description_len - amount_len)
            result += amount
            result += '\n'

        result += f'Total: {self._balance:.2f}'
        return result

def create_spend_chart(categories):
    result = ''
    result += 'Percentage spent by category\n'

    spent_amount = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += (0 - item['amount'])
        spent_amount.append(round(spent, 2))
    total_spent = round(sum(spent_amount), 2)
    spent_percents = list(map(lambda spent: (((spent / total_spent) * 10) // 1) * 10, spent_amount))


    for percent in range(100, -1, -10):
        result += '{:>3}|'.format(str(percent))
        for spent_percent in spent_percents:
            if spent_percent >= percent:
                result += ' o '
            else:
                result += '   '

        result += ' \n'

    result += ' ' * 4 + '-' * (len(spent_percents) * 3 + 1) + '\n'
    names = [category.name for category in categories]
    max_len_name = max(map(lambda name: len(name), names))

    names = [name + ' ' * (max_len_name - len(name)) for name in names]
    for i in range(max_len_name):
        result += ' ' * 4
        for name in names:
            result += f' {name[i]} '
        result += ' \n'
    return result.rstrip('\n')
