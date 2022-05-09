# Rotate the array to the left d times
#

def rotateLeft(d: int, arr: list) -> list:
    if len(arr) < 1 or d < 1:
        return arr
    

    new_arr = arr[d:] + arr[:d]
    return new_arr


d = 4
arr = [1,2,3,4,5]
print(rotateLeft(d,arr))

# 4 rotations
#[5, 1, 2, 3, 4]