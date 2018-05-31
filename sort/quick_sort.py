def sort(collection):
    quicksort(collection, 0, len(collection) - 1)
    return collection


def quicksort(collection, low, high):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :param low: index of collection from where to start to sort
    :param high: last index of collection where to end to sort
    :rtype: the same collection of item, sorted
    """
    if low < high:
        pivot = partition(collection, low, high)
        quicksort(collection, low, pivot - 1)
        quicksort(collection, pivot + 1, high)


def partition(collection, low, high):
    pivot = collection[high]
    i = low - 1
    for j in range(low, high):
        if collection[j] < pivot:
            i += 1
            collection[i], collection[j] = collection[j], collection[i]
    collection[i + 1], collection[high] = collection[high], collection[i + 1]
    return i + 1


if __name__ == '__main__':
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
