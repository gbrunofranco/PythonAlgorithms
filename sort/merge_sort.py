import copy
import math


def sort(collection):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :rtype: the same collection of item, sorted
    """
    collection_copy = copy.deepcopy(collection)
    top_down_split(collection_copy, 0, len(collection), collection)
    return collection


def top_down_split(collection_copy, begin, end, collection):
    """
    :param collection_copy: copy of collection, used to sort collection
    :param collection: collection of items (char, string, int...), unsorted
    :param begin: index from to start to sort
    :param end: index where to end to sort
    :rtype: the same collection of item, sorted
    """
    if (end - begin) < 2:
        return
    middle = math.ceil((begin + end) / 2)
    top_down_split(collection, begin, middle, collection_copy)
    top_down_split(collection, middle, end, collection_copy)
    top_down_merge(collection_copy, begin, middle, end, collection)


def top_down_merge(collection, begin, middle, end, collection_copy):
    """
    :param collection: collection of items (char, string, int...), unsorted
    :param begin: index from to start to sort
    :param middle: start of the right half
    :param end: index where to end to sort
    :param collection_copy: copy of collection, used to sort collection
    :rtype: the same collection of item, sorted
    """
    i = begin
    j = middle
    for k in range(begin, end):
        if i < middle and (j >= end or collection[i] <= collection[j]):
            collection_copy[k] = collection[i]
            i += 1
        else:
            collection_copy[k] = collection[j]
            j += 1


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
