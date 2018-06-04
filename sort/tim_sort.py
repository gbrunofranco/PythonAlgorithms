"""
Tim_sort is pretty weird for beginners so I suggest to read insertion_sort and merge_sort before this, I've tried to
explain some things in the comments but for a full explanation you should read this:
https://bugs.python.org/file4451/timsort.txt there's also this Java implementation:
http://cr.openjdk.java.net/~martin/webrevs/openjdk7/timsort/raw_files/new/src/share/classes/java/util/TimSort.java
and this wiki page: https://en.wikipedia.org/wiki/Timsort
Feel free to open an issue with suggestion to other/better sources for this amazing algorithm.
I'll describe what happens if the original is: [4, 2, 1, 3, 6, 5, 12, 11, 10, 9, 8, 7]
"""


def sort(collection):
    runs, sorted_runs = [], []
    c_length = len(collection)
    new_run = [collection[0]]
    """
    Initially new_run = [4]
    i = 1 -> It enters (2) because collection[1] < collection[0] (2 < 4) and then (2.2) because new_run isn't empty, 
    now runs is: [[4], [2]] and new_run is []
    i = 2 -> Then it enters (2) because collection[2] < collection[1] (1 < 2) and (2.1) because new_run is [] and then 
    it becomes [1]
    i = 3 -> Then it enters (3)
    i = 4 -> It enters (3) again because this run is ordered, new_run = [1, 3, 6]
    i = 5 -> (2.2) because new_run is still [1, 3, 6] and it's added to the variable runs
    i = 6 -> (3) because it's decreasing [5, 12]
    i = 7 -> (2.2)
    i = 8 -> (2.1)
    i = 9 -> (2.2)
    i = 10 -> (2.1)
    i = 11 -> (1)
    """
    for i in range(1, c_length):
        if i == c_length - 1:  # (1)
            new_run.append(collection[i])
            runs.append(new_run)
            break
        if collection[i] < collection[i - 1]:  # (2)
            if not new_run:  # (2.1), equal to new_run not []
                new_run.append(collection[i])
            else:  # (2.2)
                runs.append(new_run)
                runs.append([collection[i]])
                new_run = []
        else:  # (3)
            new_run.append(collection[i])
    """
    In the variable runs there are now multiple pieces of the original collection called runs, now the variable runs is: 
    [[4], [2], [1, 3, 6], [5], [12], [11], [10], [9], [8, 7]].
    Almost every run is sorted already, which is the purpose of the binary_search in the insertion_sort
    """
    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    """
    In runs there are now multiple sorted run. 
    In the example from before runs is is: [[4], [2], [1, 3, 6], [5], [12], [11], [10], [9], [7, 8]]
    We want the collection sorted in an ascending order so a0 >= a1 >= a2 (where aX is an element of collection) and 
    this is happening if you consider every single run by itself
    """
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    return sorted_array


def binary_search(collection, pivot, start, end):
    """
    :param collection: piece of the original collection
    :param pivot: it start from the second element of the collection and it cycle until the last element of this
        collection
    :param start: index from which it starts to search
    :param end: index at which it end up sorting
    :return: the location in the first run of the first element in the second run,
        and the location in the second run of the last element in the first run.
    """
    if start == end:
        if collection[start] > pivot:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if collection[mid] < pivot:
        return binary_search(collection, pivot, mid + 1, end)
    elif collection[mid] > pivot:
        return binary_search(collection, pivot, start, mid - 1)
    else:
        return mid


def insertion_sort(collection):
    """
    :param collection: never the full original collection, is the list to be ordered
    :return: ordered collection
    """
    c_length: int = len(collection)
    for index in range(1, c_length):
        pivot = collection[index]
        pos = binary_search(collection, pivot, 0, index - 1)
        # pos is different from index if insertion_sort is called multiple times
        collection = collection[:pos] + [pivot] + collection[pos:index] + collection[index + 1:]
    # [pivot] is needed because you can't concatenate int
    return collection


def merge(first, second):
    """
    :param first: one run, will be returned but sorted and merged
    :param second: one run, will be return but sorted and merged
    :return: the two runs merged and sorted
    """
    if not first:
        return second
    if not second:
        return first
    if first[0] < second[0]:
        return [first[0]] + merge(first[1:], second)
    return [second[0]] + merge(first, second[1:])


if __name__ == "__main__":
    user_input = input("Insert values separated by a comma.\n")
    unsorted = []
    for item in user_input.split(','):
        unsorted.append(item)
    print(sort(unsorted))
