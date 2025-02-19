## Personal Account Class

A bank account is represented by the PersonalAccount class, which records transactions and permits deposits and withdrawals. It offers ways to view the balance, make deposits and withdrawals, and print transaction histories. Additionally, it allows you to change account information such as the holder's name and account number. To manage deposits and withdrawals using the + and - operators, the class employs operator overloading.

It uses parametrized constructors and a loads of methods, and also public and private access modifiers. 

### Features

- Create a personal account with an account number and holder name.

- Deposit money into the account.

- Withdraw money from the account (ensures sufficient balance).

- View current balance at any time.

- Print transaction history (shows deposit/withdrawal details and timestamps).

- Supports operator overloading (+ for deposit, - for withdrawal).


### Example Usage
``` ruby
Account Number: 234567
Account Holder: Aiturgan
Deposit Amount: 2000 
Deposit:  2000.0 , Balance: 2000.0
Withdrawal Amount: 500
Withdraw:  500.0 , Balance: 1500.0
Another withdrawal : 1700
Withdraw:  1700.0 , Not enough balance.
Transaction History:
Amount: 2000.0 Date: 2025-02-19 23:08:29
Transaction Type: Deposit
Amount: 500.0 Date: 2025-02-19 23:08:35
Transaction Type: Withdrawal
Current Balance: 1500.0
Add some amount :300
Deposit:  300.0 , Balance: 1800.0
Substract some  amount:100
Withdraw:  100.0 , Balance: 1700.0
Account Number: 234567, Account Holder: Aiturgan, Balance: $1700.0
```
