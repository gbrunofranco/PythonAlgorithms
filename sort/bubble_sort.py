def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    c_length = len(collection)
    for i in range(c_length):
        for j in range(c_length - 1):
            if collection[j] > collection[j + 1]:
                collection[j + 1], collection[j] = collection[j], collection[j + 1]
    return collection


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
