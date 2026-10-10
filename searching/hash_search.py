# 'key' is string
def hash_key(key,size):
    new_key = 0
    for char in key:
        new_key += ord(char)

    new_key = new_key % size
    return new_key

# 'items' is list
def hash_table(items, size):
    table = [ [] for _ in range(size)]

    for item in items:
        key = hash_key(item,size)
        table[key].append(item)

    return table

# looking up target index
def hash_search(table, target, size):
    key = hash_key(target, size)

    if target in table[key]:
        return key
    else:
        return -1


