from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()



while isOn :
    choice = input(f"\nWhich drink would you chose? {menu.get_items()}: ")
    if( choice == "report"):
        print(coffee_maker.report())
        print(money_machine.report())
        continue
    elif choice == "off":
        print("Powering off")
        isOn = False
        continue
    choice = menu.find_drink(choice)
    if choice :
        if coffee_maker.is_resource_sufficient(choice):
            coffee_maker.make_coffee(choice)


