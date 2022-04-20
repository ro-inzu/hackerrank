from array import array
import copy
import heapq

# Complete the sockMerchant function below.
def sockMerchant(n : int, ar: list) -> int:
    if n < 0 or n > 100 or len(ar) < 1 or len(ar)> 100:
        return
    pairs = 0
    #used to put an element in the queue
    current = []
    #element is put in closed list after it has been checked in the queue
    closed = []
    #creates a new copy wihtout affecting the original list
    new_ar = copy.deepcopy(ar)


    while len(new_ar) != 0:
        count = 0   
        heapq.heapify(new_ar)
        print('new_ar : {}'.format(str(new_ar)))
        current_item = new_ar.pop(0)
        current.append(current_item)

        for i in range(len(ar)):
            if current[0] == ar[i] and current[0] not in closed:
                print('Pair found: current[0]: {}  == ar[i{}]: {}'.format(current[0],i,ar[i]))
                count += 1
        count = count // 2
        pairs += count
        closed_item = current.pop(0)
        closed.append(closed_item)
    return pairs


# ar = [1,2,1,2,1,3,2]
ar = [10,20,20,10,10,30,50,10,20]
n = 9
print(sockMerchant(n,ar))