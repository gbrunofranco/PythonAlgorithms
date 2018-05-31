def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    pos = 0
    c_length = len(collection)
    while pos < c_length:
        if pos == 0 or collection[pos] >= collection[pos - 1]:
            pos += 1
        else:
            collection[pos], collection[pos - 1] = collection[pos - 1], collection[pos]
            pos -= 1
    return collection


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
