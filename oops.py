class BankAccount:
    def __init__(self, account_number, account_balance, account_owner):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_owner = account_owner

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Account Balance:", self.account_balance)
        print("Account Owner:", self.account_owner)

b1 = BankAccount(123456, 10000, "Sandhiya")
b1.display_account()
