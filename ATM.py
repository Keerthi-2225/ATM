class ATM:
    def _init_(self, initial_balance=0, pin=1234):
        """
        Initialize the ATM with an initial balance and a default PIN.
        """
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []
    
    def check_pin(self, pin):
        """
        Check if the entered PIN is correct.
        """
        return pin == self.pin
    
    def change_pin(self, old_pin, new_pin):
        """
        Change the PIN if the old PIN is correct.
        """
        if self.check_pin(old_pin):
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect PIN."
    
    def balance_inquiry(self):
        """
        Return the current balance.
        """
        return f"Your current balance is: ${self.balance}"
    
    def deposit(self, amount):
        """
        Deposit the specified amount and log the transaction.
        """
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"${amount} deposited successfully."
    
    def withdraw(self, amount, pin):
        """
        Withdraw the specified amount if the PIN is correct and sufficient funds are available.
        """
        if not self.check_pin(pin):
            return "Incorrect PIN."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount}")
        return f"${amount} withdrawn successfully."
    
    def get_transaction_history(self):
        """
        Return the list of transactions or a message if there are no transactions.
        """
        return self.transaction_history if self.transaction_history else "No transactions yet."

# Create an ATM instance
atm = ATM(initial_balance=500)
# Demonstration of functionalities
print(atm.balance_inquiry())  # Balance inquiry
print(atm.deposit(200))       # Deposit
print(atm.withdraw(100, 1234))# Withdrawal with correct PIN
print(atm.withdraw(50, 0000)) # Withdrawal with incorrect PIN
print(atm.change_pin(1234, 5678)) # Change PIN
print(atm.change_pin(1234, 1111)) # Attempt to change PIN with incorrect old PIN
print(atm.get_transaction_history()) # Get transaction history