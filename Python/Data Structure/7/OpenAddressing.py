M = 13  # hash table's size tends to be used as prime number when key%M is used
# if so, the probability of getting the same key would decrease rather than using non-prime number
table = [0] * M  # create hash table

def hashFunction(key): 
    return key % M

def getLinear(v, i):
    return (v + i) % M  # calculate address of value

def hashFunction2(key): 
    return 11 - (key % 11)  # (biggest prime number smaller than M) - (key % (biggest prime number smaller than M))

def search(key):
    v = hashFunction(key)
    i = 0
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)

        if table[b] == key:
            return b
        elif table[b] == 0:  # If an empty spot is found, the key is not in the table
            return 0
        else:
            i += 1
    return 0  # If the entire table is searched and the key is not found

def delete(key):
    v = hashFunction(key)
    i = 0
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)

        if table[b] == 0:  # If an empty spot is found, the key is not in the table
            return 0
        
        elif table[b] == key:
            table[b] = 0  # delete the key by setting it to 0
            return b
        
        else:
            i += 1
    return 0  # If the entire table is searched and the key is not found

def insert(key):
    v = hashFunction(key)  # get the address for key
    i = 0
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)
        if table[b] == 0:
            table[b] = key  # insert value when address is empty
            return
        else:
            i += 1  # else, move to right until an empty address appears

def getQuadratic(v, i): 
    return (v + i*i) % M

def getDouble(v, i, key): 
    return (v + i * hashFunction2(key)) % M

def display():
    print()
    print("Bucket Key")
    print("==========")
    for i in range(M):
        print(f"HT{i} : {table[i]}")

if __name__ == '__main__':
    data = [45, 27, 88, 9, 71, 68, 46, 38, 24]
    for d in data:
        insert(d)

    display()
    print()
    print(f"Search(46) --- > {search(46)}")
    print(f"Search(39) --- > {search(39)}")
    print(f"Delete(46) --- > {delete(46)}")
    print(f"Delete(39) --- > {delete(39)}")
    display()
    print(f"Search(46) --- > {search(46)}")

