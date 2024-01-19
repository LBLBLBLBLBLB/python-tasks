def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory


def displayInventory(inventory):
    total = 0
    result = "Inventory:"
    for key, val in inventory.items():
        result += f"\n{val} {key}"
        total += val
    result += f"\nTotal number of items: {total}"
    return result


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
print(displayInventory(inv))