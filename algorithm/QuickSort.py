
__author__ = 'phoenix'


def partition(part_list, start, end):
    i = start - 1
    pivot = part_list[end]
    for j in range(start, end-1):
        if part_list[j] < pivot:
            i += 1
            part_list[j], part_list[i] = part_list[i], part_list[j]
    part_list[i+1], part_list[end] = part_list[end], part_list[i+1]
    return i+1


def quick_sort(unsorted_list, start, end):
    if start < end:
        p = partition(unsorted_list, start, end)
        quick_sort(unsorted_list, start, p-1)
        quick_sort(unsorted_list, p+1, end)
    else:
        return

if __name__ == "__main__":
    import time
    start = time.clock()
    array = [2, 4, 32, 64, 34, 78, 23, 2345, 2345, 12, 1, 3]
    quick_sort(array, 0, len(array)-1)
    stop = time.clock()
    print(array)
    print("total time used %(times)f" % {"times": stop-start})
