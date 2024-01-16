usd_buy = 38.0000
usd_sell = 38.4497

eur_buy = 41.5000
eur_sell = 42.1496

pln_buy = 9.7409
pln_sell = 9.9545

try_buy = 1.2994
try_sell = 1.3550

def display_rates(buy_rate, sell_rate, currency_name):
    print(f"\n{currency_name} buying rate is {buy_rate} and selling rate is {sell_rate}")

def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
            
def perform_exchange(buy_rate, sell_rate, currency_name):
    while True:
        print(f"\nDo you want to Buy or Sell {currency_name}? (Type 'Buy' or 'Sell')")
        buy_sell_choice = input()

        if buy_sell_choice.lower() == "end":
            exit_program()

        if buy_sell_choice.lower() == "buy":
            bank_budget = get_float_input(f"\nHow much {currency_name} do you want to buy? ")
            exchange_buy = round(sell_rate * bank_budget, 2)
            print(f"\nSo, you need to pay {exchange_buy} UAH.")
            break
        elif buy_sell_choice.lower() == "sell":
            client_budget = get_float_input(f"\nHow much {currency_name} do you want to sell? ")
            exchange_sell = round(buy_rate * client_budget, 2)
            print(f"\nSo, you will get: {exchange_sell} UAH.")
            break
        else:
            print("Choose one of the options: Buy or Sell.")

def exit_program():
    print("\nExiting the program.")
    exit()

while True:

    while True:
        print("\n1. USD \n2. EUR \n3. PLN \n4. TRY \nSelect currency you want to Buy or Sell: ")
        currency_choice = input()

        if currency_choice.lower() == "end":
            exit_program()

        if currency_choice.isdigit() and 1 <= int(currency_choice) <= 4:
            break
        else:
            print(f"\nInvalid choice! Choose a number from 1 to 4.")

    currency_choice = int(currency_choice)

    if currency_choice == 1:
        display_rates(usd_buy, usd_sell, "US Dollar")
        currency_choice_name = "USD"
        currency_buy_rate = usd_buy
        currency_sell_rate = usd_sell
    elif currency_choice == 2:
        display_rates(eur_buy, eur_sell, "Euro")
        currency_choice_name = "EUR"
        currency_buy_rate = eur_buy
        currency_sell_rate = eur_sell
    elif currency_choice == 3:
        display_rates(pln_buy, pln_sell, "Polish zloty")
        currency_choice_name = "PLN"
        currency_buy_rate = pln_buy
        currency_sell_rate = pln_sell
    elif currency_choice == 4:
        display_rates(try_buy, try_sell, "Turkish lira")
        currency_choice_name = "TRY"
        currency_buy_rate = try_buy
        currency_sell_rate = try_sell

    perform_exchange(currency_buy_rate, currency_sell_rate, currency_choice_name)

    another_exchange = input("Do you want to perform another currency exchange? (yes/no): ")
    if another_exchange.lower() != 'yes':
        exit_program()
