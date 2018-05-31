def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    c_length = len(collection)
    for i in range(1, c_length):
        pivot = collection[i]
        j = i-1
        while j >= 0 and collection[j] > pivot:
            collection[j+1], collection[j] = collection[j], collection[j+1]
            j -= 1
        collection[j+1] = pivot
    return collection


if __name__ == '__main__':
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
