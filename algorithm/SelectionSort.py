"""
It's my train of algorithm on python.
address: http://visualgo.net/sorting.html
"""

__author__ = 'phoenix'


def selectionsort(unsortedlist):
    for i in range(0, len(unsortedlist)):
        minindex = i
        for j in range(i+1, len(unsortedlist)):
            if unsortedlist[minindex] > unsortedlist[j]:
                minindex = j
        unsortedlist[i], unsortedlist[minindex] = unsortedlist[minindex], unsortedlist[i]
    return unsortedlist

if __name__ == "__main__":
    import time
    start = time.clock()
    array = [2, 4, 32, 64, 34, 78, 23, 2345, 2345, 12, 1, 3]
    selectionsort(array)
    stop = time.clock()
    print(array)
    print("total time used %(times)f" % {"times": stop-start})