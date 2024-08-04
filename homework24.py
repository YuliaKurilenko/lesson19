import threading
class BankAccount:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f" Deposited {amount}, new balance is {self.amount}")
        return
    def withdraw(self, amount):
        self.amount -= amount
        print(f" Withdrew {amount}, new balance is {self.amount}")
        return
account = BankAccount(1000)
def deposit_task(account, amount):
    with lock:
        for _ in range(5):
            account.deposit(amount)
def withdraw_task(account,amount):
    with lock:
        for _ in range(5):
            account.withdraw(amount)
lock = threading.RLock()
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))
deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()
