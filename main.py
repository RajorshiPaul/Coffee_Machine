from data import resources
import helper as hp


def main():
    # Initialize coffee machine
    stock = resources
    stock['money'] = 0

    while not hp.is_empty(stock):
        order = input("What would you like? (espresso/ latte/ cappuccino). "
                      "Type 'report' for report. ")

        if order == 'report':
            hp.print_report(stock)
            continue

        if hp.check_resources(stock, order):
            hp.process_coins(order)
            stock = hp.update_resources(stock, order)

    print("Coffee machine is empty. Try again later.")


if __name__ == '__main__':
    main()