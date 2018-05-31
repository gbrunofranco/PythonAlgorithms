import math


def sort(collection):
    c_length = len(collection)
    gap = len(collection)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = math.floor(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < c_length:
            if collection[i] > collection[i + gap]:
                collection[i], collection[i + gap] = collection[i + gap], collection[i]
                sorted = False
            i += 1
    return collection


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
