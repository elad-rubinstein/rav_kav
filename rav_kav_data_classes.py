"""
Manage a Rav-Kav card and execute different tasks on it.
"""


from dataclasses import dataclass


@dataclass
class Rav_kav:
    money_spent: float = 0
    balance: float = 0

    def add_money(self, money: float) -> None:
        """
        Add money to the current balance and print the status
        :param money: The amount of money to be added.
        """
        self.balance += money
        print(f"{money}$ were added to your account!")
        print(f"your account balance is now {self.balance}$")

    def spend_money(self, money: float) -> None:
        """
        Spend money from the current balance and print the status
        :param money: The amount of money to be spent.
        """
        self.balance -= money
        self.money_spent += money
        print(f"{money}$ were spent from your account!")
        print(f"your account balance is now {self.balance}$")


def main():
    """
    Execute a loop in which every time the user should choose a task to perform
   """
    count = 1
    card1 = Rav_kav()
    while True:
        print(f"Choose action for day {count}/30:\n1. Add money\n2. Spend money"
              "\n3. Exit")
        action_num = int(input())
        if action_num == 3:
            print("Exiting!")
            exit()
        elif action_num == 2:
            print("please enter the amout of money you want to spend:", end=" ")
            card1.spend_money(float(input()))
        else:
            print("please enter the amout of money you want to add:", end=" ")
            card1.add_money(float(input()))
        if count == 10:
            card1.balance = card1.money_spent
            print(f"30 days passed, your account balance is now"
                  f" {card1.balance}$!")
            count = 1
        count += 1      


if __name__ == '__main__':
    main()
