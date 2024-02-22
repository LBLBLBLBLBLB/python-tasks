game_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    result = "Inventory"
    for key, val in inventory.items():
        result += f"\n{key} {val}"
    return result


print(displayInventory(game_inventory))
