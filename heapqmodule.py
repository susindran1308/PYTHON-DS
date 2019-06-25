import heapq as heap

L = []

heap.heappush(L,30)
heap.heappush(L,10)
heap.heappush(L,20)
heap.heappush(L,60)
heap.heappush(L,40)
heap.heappush(L,30)
heap.heappush(L,50)
heap.heappush(L,90)
print(L)

heap.heappop(L)
print(L)

heap.heappushpop(L, 5)
print(L)

L1 = heap.nlargest(3, L)
print(L1)

L2 = heap.nsmallest(4, L)
print(L2)


L3 = [54, 67, 89, 34,56,2,4,6]

heap.heapify(L3)
print(L3)