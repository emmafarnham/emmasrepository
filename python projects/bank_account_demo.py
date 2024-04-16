from bank_account import BankAccount

account1=BankAccount("12345")
account2=BankAccount("5798", 750.00)
account3=BankAccount("4283", 2000.00)

print(account1)
print(account2)
print(account3)


account1.deposit(108.56)
account1.withdraw(200.00)
account3.withdraw(100.65)
