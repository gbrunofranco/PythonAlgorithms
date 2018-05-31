def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    c_length = len(collection)
    for i in range(c_length):
        min = i
        for j in range(i+1, c_length):
            if collection[min] > collection[j]:
                min = j
        collection[i], collection[min] = collection[min], collection[i]
    return collection


if __name__ == '__main__':
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
