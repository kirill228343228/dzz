class bankAccount:
    account_number = ""
    balance = 0
    deposit = 0
    withdraw = 0

    def __init__(self, account_number, balance, deposit, withdraw):
        self.account_number = account_number
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw

    def print_stats(self):
        print(f"номер картки ({self.account_number})")
        print(f"баланс: {self.balance}")
        print(f"покласти гроші: {self.deposit}")
        print(f"зняти гроші: {self.withdraw}")