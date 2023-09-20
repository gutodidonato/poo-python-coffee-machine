from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def checar_bebida(drink):
    order = menu.find_drink(drink)
    while order == None:
        drink = input("What drink you want? ")
        order = menu.find_drink(drink)
    order = menu.find_drink(drink)
    resource = coffee_maker.is_resource_sufficient(order)
    if resource == False:
        drink = ""
        checar_bebida(drink)
    return order


    
print(logo)
while True:
    consumer = input("You are a consumer? ")
    if consumer == "no":
        money_machine.report()
        coffee_maker.report()
        print("\n")
    pedido = input("Are you ready? ")
    if pedido == "off":
        print("Serviço Encerrado")
        break
    print(f"Our drinks are: {menu.get_items()}")
    drink = input("What drink you want? ")
    drink_certo = checar_bebida(drink)
    money_machine.make_payment(drink_certo.cost)
    coffee_maker.make_coffee(drink_certo)
    print("\n")
    