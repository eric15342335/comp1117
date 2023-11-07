def print_inventory(inventory):
    """Print the inventory to the console."""
    n_type = len(inventory)
    print(f"Inventory: {n_type} type(s) of drinks available")
    for k, v in inventory.items():
        print(f"Name: {k}, Price: ${v[0]}, Stock: {v[1]}")


def read_inventory():
    """
    Read the inventory from the input and return it as a dictionary.
       e.g. {'Sprite':[4, 3], 'Orange_juice':[3, 1]}. 
            This means there are three $4 Sprite and one $3 Oriange_juice in the inventory.
    """
    # Begin of your implementation ------
 
    # End of your implementation ------


def insert_coin(total_coin, coin_value):
    # Begin of your implementation ------

    # End of your implementation ------


def return_coins(total_coin):
    # Begin of your implementation ------

    # End of your implementation ------


def buy_drink(inventory, total_coin, drink_name):
    # Begin of your implementation ------

    # End of your implementation ------


if __name__ =='__main__':
    inventory = read_inventory()
    print_inventory(inventory)
    total_coin = 0
    while True:
        s = input()
        if s.startswith('Insert'):
            vals =s.split(' ')
            total_coin = insert_coin(total_coin, int(vals[1]))
        elif s.startswith('Return'):
            total_coin = return_coins(total_coin)
        elif s.startswith('Buy'):
            vals =s.split(' ')
            inventory, total_coin = buy_drink(inventory, total_coin, vals[1])
        elif s == "Exit":
            if total_coin > 0:
                total_coin = return_coins(total_coin)
            break
    print_inventory(inventory)