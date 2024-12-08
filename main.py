from BankAccount import bankAccount
import time

c = 1000

numb = bankAccount(account_number=797304234301, balance=c, deposit=0, withdraw=0)
print(f"номер картки (797304234301)")
print("")
print("якщо вихочете покласти гроші натисніть: 1")
print("якщо вихочете зняти грроші натисніть: 2")
print("якщо вихочете дізнатися баланс натисніть: 3")
print("")
a = int(input("Введіть число: "))
if a == 1:
    b = int(input("скіки хочете покласти грошей:"))
    print("")
    numb = bankAccount(account_number=797304234301, balance=c, deposit=b, withdraw=0)
    numb.print_stats()
    time.sleep(2)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    numb = bankAccount(account_number=797304234301, balance=c+b, deposit=0, withdraw=0)
    numb.print_stats()

if a == 2:
    b = int(input("скіки хочете зняти грошей:"))
    print("")
    numb = bankAccount(account_number=797304234301, balance=c, deposit=0, withdraw=b)
    numb.print_stats()
    time.sleep(2)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    numb = bankAccount(account_number=797304234301, balance=c - b, deposit=0, withdraw=0)
    numb.print_stats()

if a == 3:
    numb = bankAccount(account_number=797304234301, balance=c, deposit=0, withdraw=0)
    numb.print_stats()


