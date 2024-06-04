def validate_account(account_number, accounts):
    if len(account_number) != 16:
        return False, None
    if account_number in accounts:
        return True, accounts[account_number]
    else:
        return False, None