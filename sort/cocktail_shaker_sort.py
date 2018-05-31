def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    swapped = True
    while swapped:
        swapped = False
        c_length = len(collection)
        for i in range(c_length - 1):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(c_length - 2, -1, -1):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i+1], collection[i]
                swapped = True
    return collection


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
