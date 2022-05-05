def reverseArray(a):
    if len(a) < 1 or len(a) > 1000:
        return
        
    return a[::-1]



arr = [9,8,2,3]
print(f'reversed arr: {reverseArray(arr)}')