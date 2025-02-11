from personal_account import PersonalAccount

# Testing the code and cases
account_number = int(input('Account Number: '))
account_holder = input('Account Holder: ')
account = PersonalAccount(account_number, account_holder)

deposit_amount = float(input('Deposit Amount: '))
account.deposit(deposit_amount)

withdraw_amount = float(input('Withdrawal Amount: '))
account.withdraw(withdraw_amount)
account.withdraw(float(input("Another withdrawal:")))


print('Transaction History:')
account.print_transaction_history()

print(f'Current Balance: {account.get_balance()}')

account+float(input('Add some amount:'))
account-float(input('Substract some amount:'))
print(account)


