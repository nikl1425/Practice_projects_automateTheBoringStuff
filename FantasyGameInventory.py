PlayerInventory = {'arrow': 12,
                   'gold': 42,
                   'rope': 1,
                   'torch': 6,
                   'dagger': 1}
DragonLoot = ['gold', 'dagger', 'ruby', 'gold', 'gold']


def displayInventory(inventory):
    print(inventory)
    countItems = 0
    for k, v in inventory.items():
        countItems += v
        print(str(v) + " " + str(k))
    print("total number of items " + str(countItems))


def addToInventory(inventory, loot):
   for element in loot:
       if element not in inventory.keys():
           inventory[element] = 1
       elif element in inventory.keys():
           inventory[element] += 1



displayInventory(PlayerInventory)
addToInventory(PlayerInventory, DragonLoot)
displayInventory(PlayerInventory)
