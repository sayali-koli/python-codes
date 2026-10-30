class insufficientfundError(Exception):
    pass


def withdraw_money(balance, withdraw_amount):
    if withdraw_amount > balance:
        raise insufficientfundError("not enough balance")
    print(f"remaining balance : {balance-withdraw_amount}")


try:
    withdraw_money(1000, 5000)
except insufficientfundError as e:
    print(type(e).__name__)
    print(f"error message : {e}")
except insufficientfundError as e:
    print(type(e).__name__)
    print(f"error message : {e}")
