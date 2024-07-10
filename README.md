ATM Code Documentation
Introduction:
This is a Python program that simulates an ATM machine.

Classes:
- ATM: The main class that represents the ATM machine.

Methods:
- __init__: Initializes the ATM with a balance and PIN.
- check_balance: Displays the current balance.
- withdraw: Withdraws cash from the account.
- deposit: Deposits cash into the account.
- change_pin: Changes the PIN for the account.
- transaction_history: Displays the transaction history.

Functions:
- main: The main function that runs the ATM program.
Variables:
- balance: The current balance of the account.
- pin: The PIN for the account.
- history: The transaction history.
Notes:
- This program uses a simple PIN system for authentication.
- The transaction history is stored in a list.

### Explanation of the Code:
1. **Class Initialization (__init__): 
   - Initializes the ATM with an initial balance, a default PIN, and an empty transaction history list.

2. **Check PIN (check_pin): 
   - Verifies if the entered PIN matches the stored PIN.

3. **Change PIN (change_pin): 
   - Allows changing the PIN if the old PIN is entered correctly.

4. **Balance Inquiry (balance_inquiry): 
   - Returns the current balance of the account.

5. **Deposit (deposit): 
   - Increases the balance by the deposited amount and logs the transaction.

6. **Withdraw (withdraw): 
   - Decreases the balance by the withdrawal amount if the entered PIN is correct and there are sufficient funds, and logs the transaction.

7. **Transaction History (get_transaction_history): 
   - Returns a list of all transactions or a message if no transactions have been made.

This code provides a basic simulation of an ATM machine, handling common operations such as balance inquiry, deposit, withdrawal, PIN change, and transaction history logging.
