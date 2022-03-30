stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}       

def displayInventory(inventory):
    count = 0
    for keys,values in stuff.items():
        count = count + values
        print (values, keys)

    print ('total number of items: ', count )

    # your code goes here

#displayInventory(stuff)