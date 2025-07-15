from collections import Counter
import heapq

def topKFrequentElements(num, k):
    count = Counter(num)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (-freq, num))
    result = []
    for i in range(k):
        freq, num = heapq.heappop(heap)
        result.append(num)
    return result