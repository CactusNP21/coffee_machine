def coffee_machine_manager():
    water, milk, beans, cups, money = 400, 540, 120, 9, 550

    def coffee_machine_storage(water_change=0, milk_change=0, beans_change=0, cups_change=0, money_change=0):
        nonlocal water, milk, beans, cups, money
        water += water_change
        milk += milk_change
        beans += beans_change
        cups += cups_change
        money += money_change

    def coffee_machine_logic(water_minus=0, milk_minus=0, beans_minus=0, cups_minus=0, money_plus=0):
        water_available = water + water_minus
        milk_available = milk + milk_minus
        beans_available = beans + beans_minus
        cups_available = cups + cups_minus
        xs = [water_available, milk_available, beans_available, cups_available]
        xs_min = min(xs)
        if xs_min < 0:
            if water_available < 0:
                print("Sorry, not enough water!")
            if milk_available < 0:
                print("Sorry, not enough milk!")
            if beans_available < 0:
                print("Sorry, not enough coffee beans!")
            if cups_available < 0:
                print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            coffee_machine_storage(water_change=water_minus, milk_change=milk_minus, beans_change=beans_minus,
                                   cups_change=cups_minus, money_change=money_plus)

    def coffee_machine_status():
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money
        """.format(water, milk, beans, cups, money))

    def buy():
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        user = input()
        if 'back' not in user:
            if '1' in user:
                coffee_machine_logic(water_minus=-250, beans_minus=-16, money_plus=4, cups_minus=-1)
            elif '2' in user:
                coffee_machine_logic(water_minus=-350, milk_minus=-75, beans_minus=-20, money_plus=7, cups_minus=-1)
            elif '3' in user:
                coffee_machine_logic(water_minus=-200, milk_minus=-100, beans_minus=-12, money_plus=6, cups_minus=-1)
        else:
            return

    def fill():
        print('Write how many ml of water you want to add:')
        coffee_machine_storage(water_change=int(input()))
        print("Write how many ml of milk you want to add:")
        coffee_machine_storage(milk_change=int(input()))
        print("Write how many grams of coffee beans you want to add:")
        coffee_machine_storage(beans_change=int(input()))
        print("Write how many disposable coffee cups you want to add:")
        coffee_machine_storage(cups_change=int(input()))

    def take():
        print('I gave you {}'.format(money))
        coffee_machine_storage(money_change=-money)

    def actions():
        print('Write action (buy, fill, take, remaining, exit):')
        user = input()
        if 'buy' in user:
            buy()
            return 1
        elif 'fill' in user:
            fill()
            return 1
        elif 'take' in user:
            take()
            return 1
        elif 'remaining' in user:
            coffee_machine_status()
            return 1
        elif 'exit' in user:
            return 0

    condition = True
    while condition:
        condition = actions()


def main():
    coffee_machine_manager()


if __name__ == '__main__':
    main()
