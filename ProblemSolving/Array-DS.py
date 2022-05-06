# slicing implementation
def reverseArray(a):
    if len(a) < 1 or len(a) > 1000:
        return
        
    return a[::-1]


# for loop implementation
def reverseArray2(a):
    my_list = []
    for i in range(1,len(a) + 1):
        my_list.append(a[-i])
    return my_list



arr = [9,8,2,3]
print(f'reversed arr using slicing: {reverseArray(arr)}')
print(f'reversed arr using a for loop: {reverseArray2(arr)}')