from prettytable import PrettyTable
from time import sleep
import os

class CoffeeMachine():
    coffees = ["espresso", "latte", "cappuccino"]
    coffee_resources = {
        "espresso":     {
                "water": 100,
                "milk": 0,
                "coffee": 200,
                "cost": 1.0
            },
        "latte":     {
                "water": 200,
                "milk": 200,
                "coffee": 100,
                "cost": 2.5
            },
        "cappuccino":     {
                "water": 150,
                "milk": 100,
                "coffee": 150,
                "cost": 1.5
            }
    }
    resources = None
    water = 0
    milk = 0
    coffee = 0
    profit = 0.0

    money = 0.0
    powered_on = False

    def __init__(self, water, milk, coffee) -> None:
        self.resources = PrettyTable()
        self.resources.field_names = ["Water", "Milk", "Coffee", "Money"]
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def click_on_off(self):
        self.powered_on = not self.powered_on
        if self.powered_on:
            self.run_machine()
        else:
            if self.money > 0:
                self.cash_out()
                sleep(0.5)
            print("Shutting down...")
            sleep(0.5)

    def run_machine(self):
        while True:
            self.clear_display()
            print(f"Your balance: {self.money}")
            cash_in = float(input("Please insert some money: "))
            self.insert_money(cash_in)
            self.clear_display()
            print(f"Your balance: {self.money}")
            user_choice = int(input("What would you like? (0. espresso | 1. latte | 2. cappuccino): "))
            if user_choice == 3:
                self.report()
                self.clear_report()
                input()
            elif user_choice == 4:
                self.click_on_off()
                break
            elif user_choice == 0 or user_choice == 1 or user_choice == 2:
                if self.check_resources(user_choice):
                    if self.transaction(user_choice):
                        print(f"Preparing your {self.coffees[user_choice]}...")
                        self.make_coffee()
                        print("Your coffee is done.")
                        input("Please remove the cup from the tray.")
            else:
                input("Invalid input. Try again.")

    def check_resources(self, coffee_choice):
        coffee = self.coffees[coffee_choice]
        resource_necessary = self.coffee_resources[coffee]
        if (resource_necessary["water"] <= self.water and 
            resource_necessary["milk"] <= self.milk and 
            resource_necessary["coffee"] <= self.coffee):
            return True
        not_enough = ""
        if resource_necessary["water"] > self.water:
            not_enough += "Not enough water. "
        if resource_necessary["milk"] > self.milk:
            not_enough += "Not enough milk. "
        if resource_necessary["coffee"] > self.coffee:
            not_enough += "Not enough coffee beans."
        input(not_enough)
        return False

    def transaction(self, coffee_choice):
        coffee = self.coffees[coffee_choice]
        resource = self.coffee_resources[coffee]
        cost = resource["cost"]
        if cost <= self.money:
            self.profit += cost
            self.money -= cost
            return True
        print("Not enough balance.")
        input(f"Coffee cost: {cost}. Your balance: {self.money}")
        return False
    
    def insert_money(self, change):
        self.money += change

    def cash_out(self):
        print(f"Cash back: {self.money}")
        self.money = 0

    def make_coffee(self):
        for _ in range(5):
            sleep(0.25)
            print(".")
            sleep(0.25)

    def report(self):
        self.resources.add_row(
            [self.water, self.milk, self.coffee, self.profit]
        )
        print(self.resources)

    def clear_report(self):
        self.resources.clear_rows()
    
    def clear_display(self):
        os.system('cls')



if __name__ == "__main__":
    machine = CoffeeMachine(1000, 1000, 1000)
    machine.click_on_off()
    machine.report()
    input()


''' 
    REFLECTIONS:
    So, there's some issues with this. Resources arent being subtracted at this time for example.
    I feel like I did not do a very good job of keeping the OOP principles clean.
    For example, maybe another class for Coffee()... Factory pattern?
    But I wrote this while being very exhausted. And I had 3 coffees today, so my teeth are perma-clenched right now :(
    Feels shit man. But other than that, the program works like a dream. 
    Oh and you can't replenish resources. But I dont give a fuck anymore.
'''

'''
    Angela Yu implemented 3 Classes, not just a single one...
    Class 1: Money Machine
    Class 2: Coffee Maker
    Class 3: Menu

    Consider. What are each classes attributes and what can it do?
    Class 1: Money Machine
        Attributes:
            Profit
            Change
        Methods:
            Transaction (take payment)
            Calculate change
            print report on profit
            print report on change
    
    Class 2: Coffee Maker
        Attributes:
            bool for whether its on or not.
            menu object
            money machine object
            resources (water, milk, coffee)
        Methods:
            ask user for input
            check sufficient resources
            make coffee
    Class 3: Menu
        Attributes:
            Coffees (Espresso, Latte, cappuccino)
            resources needed for each coffee
        Methods:
            Show Menu
            Get requirements for specific coffee

    There is even the elusive 4th Class: MenuItem()
            
'''