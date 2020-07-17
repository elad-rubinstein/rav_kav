"""
Manage a Rav-Kav card and execute different tasks on it.
"""


from typing import Tuple


def add_money(account_balance: float) -> float:

    """
    Add money to the current balance and print the status
    :param account_balance: The user's account balance.
    :return: The user's account balance.
    """
    print("Please enter the amount of money you want to add to the card:",
          end=" ")
    money_amount = float(input())
    account_balance += money_amount
    print(f"{money_amount}$ were added to your account!")
    print(f"your account balance is now {account_balance}$")
    return account_balance


def spend_money(account_balance: float, sum_of_expenses: float) -> Tuple[float,
                                                                         float]:

    """
    Spend money from the current balance and print the status
    :param account_balance: The user's account balance.
    :param sum_of_expenses: The user's current sum of expenses.
    :return: The user's account balance and sum of expenses.
    """
    print("Please enter the amount of money you want to spend:", end=" ")
    money_amount = float(input())
    sum_of_expenses += money_amount
    account_balance -= money_amount
    print(f"{money_amount}$ were spent from your account!")
    print(f"your account balance is now {account_balance}$")
    return account_balance, sum_of_expenses


def main():

    """
    Execute a loop in which every time the user should choose a task to perform
    """
    count = 1
    account_balance = 0
    sum_of_expenses = 0
    while True:
        print(f"Choose action for day {count}/30:\n1. Add money\n2. Spend money"
              "\n3. Exit")
        action_num = int(input())
        if action_num == 3:
            print("Exiting!")
            exit()
        elif action_num == 2:
            account_balance, sum_of_expenses = \
                spend_money(account_balance, sum_of_expenses)
        else:
            account_balance = add_money(account_balance)
        if count == 30:
            account_balance = sum_of_expenses
            print(f"30 days passed, your account balance is now"
                  f" {account_balance}$!")
            count = 1
        count += 1


if __name__ == '__main__':
    main()
