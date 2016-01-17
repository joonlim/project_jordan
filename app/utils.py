

# Takes a list as input and pushes every two items of that list into a new list
# as pairs of items and returns the new list. If there is an odd number of
# items, the last pair has only one item in the list.
# Ex: [1,2,3,4,5,6,7] -> [[1,2],[3,4],[5,6],[7]]
def group_into_pairs(items):
    pairs = list()

    i = 0
    while i < len(items):
        pair = list()
        pair.append(items[i])
        # Check for next items
        i += 1
        if i < len(items):
            pair.append(items[i])
        pairs.append(pair)
        i += 1

    return pairs
