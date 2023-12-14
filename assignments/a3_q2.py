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
    user = input()
    inv_dict = dict()
    while user != "-1":
        user = user.split()
        inv_dict[user[0]] = [int(user[1]), int(user[2])]
        user = input()
    return inv_dict
    # End of your implementation ------


def insert_coin(total_coin, coin_value):
    # Begin of your implementation ------
    total = total_coin + coin_value
    print(f"Inserted a ${coin_value} coin. Total: ${total}.")
    return total
    # End of your implementation ------


def return_coins(total_coin):
    # Begin of your implementation ------
    returned = {10: 0, 5: 0, 2: 0, 1: 0}
    total_returned = 0
    for i in returned.keys():
        while True:
            if total_coin - i >= 0:
                total_coin -= i
                returned[i] += 1
                total_returned += i
            else:
                break
    print("Return", end="")
    if sum(returned.values()) > 0:
        text = []
        for i in returned.keys():
            if returned[i] != 0:
                text.append(f" {returned[i]} x ${i}")
        print(",".join(text) + f". Total return: ${total_returned}.")
    else:
        print(" no coin!")
    return 0
    # End of your implementation ------


def buy_drink(inventory, total_coin, drink_name):
    # Begin of your implementation ------
    # note: inventory dictionary: {name:[price, quantity]}
    price, quantity = inventory[drink_name][0], inventory[drink_name][1]
    # Inserted credit is not enough to buy the drink.
    if price <= total_coin:
        # The drink is out of stock
        # ... you can assume they would not happen simultaneously
        # in our test case ...
        if quantity > 0:
            total_coin -= price
            inventory[drink_name][1] -= 1
            print(f"Dropped {drink_name}. Paid ${price}. Remain ${total_coin}.")
        else:
            print(f"Out of stock! {drink_name} is sold out.")
    else:
        print(
            f"Insufficient money to buy {drink_name}! Inserted: ${total_coin}, Required: ${price}."
        )
    return inventory, total_coin
    # End of your implementation ------


if __name__ == "__main__":
    inventory = read_inventory()
    print_inventory(inventory)
    total_coin = 0
    while True:
        s = input()
        if s.startswith("Insert"):
            vals = s.split(" ")
            total_coin = insert_coin(total_coin, int(vals[1]))
        elif s.startswith("Return"):
            total_coin = return_coins(total_coin)
        elif s.startswith("Buy"):
            vals = s.split(" ")
            inventory, total_coin = buy_drink(inventory, total_coin, vals[1])
        elif s == "Exit":
            if total_coin > 0:
                total_coin = return_coins(total_coin)
            break
    print_inventory(inventory)
