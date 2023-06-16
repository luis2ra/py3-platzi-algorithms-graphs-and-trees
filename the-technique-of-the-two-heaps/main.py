import heapq


numbers = [8, 7, 1, 5, 3, 8, 11, 6, 14]
# numbers = [100, 12, 8, 3, 6, 7, 2]

nums = sorted(numbers)

min_heap = []
max_heap = []


def insert_in_minheap(val):
    heapq.heappush(min_heap, val)


def insert_in_maxheap(val):
    heapq.heappush(max_heap, val * -1)


def print_median():
    if len(min_heap) > len(max_heap):
        print(heapq.nsmallest(1, min_heap)[0])
    elif len(max_heap) > len(min_heap):
        print((heapq.nsmallest(1, max_heap)[0] * -1))
    else:
        median = (heapq.nsmallest(1, min_heap)[0] + (heapq.nsmallest(1, max_heap)[0] * -1)) / 2
        print(median)


def run():
    for index, value in enumerate(nums):
        if index == 0:
            print(value)
            insert_in_maxheap(value)
        else:
            if value >= (heapq.nsmallest(1, max_heap)[0] * -1):
                insert_in_minheap(value)
            else:
                insert_in_maxheap(value)
            if len(min_heap) - len(max_heap) > 1:
                insert_in_maxheap(heapq.heappop(min_heap))
            elif len(max_heap) - len(min_heap) > 1:
                insert_in_minheap(heapq.heappop(max_heap) * -1)
            print_median


if __name__ == "__main__":
    run()
