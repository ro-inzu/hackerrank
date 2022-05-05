# sol 1

def hourglassSum(arr):
    my_list = []

    for i in range(len(arr)):
        print(f'index-i: {i} sub_arr: {arr[i]}')
        for j in range(len(arr[i])):
            # first row of hourglass checks thats len of 3
            total = 0
            # first row of hourglass
            if len(arr[i][j:j + 3]) == 3:   # only want to iterate if there are at least 3 numbs left in the sub arr
                print(f'\tindex-j: {j} sub_arr: {arr[i][j:j + 3]}')
                print(f'\t\trow {i} || sum: {sum(arr[i][j:j + 3])}')
                first_row = sum(arr[i][j:j + 3])
                # mid section of hourglass go to the next row
                if len(arr[i]) > i + 1: # checks that there is a next position in the arr
                    print(f'\tmid section: {arr[i + 1]}')
                    print(f'\t\t mid val: {arr[i + 1][j + 1]}')
                    mid_row = arr[i + 1][j + 1]
                # last row of hourglass
                if len(arr[i][j:j + 3]) == 3 and len(arr[i]) > i + 2:   # checks that there are 2 positions ahead in the arr and that there are at least 3 numbs left
                    print(f'\t\tlast row {i} || last row: {arr[i+ 2][j:j + 3]}')
                    print(f'\t\tlast row {i} || sum: {sum(arr[i+ 2][j:j + 3])}')
                    last_row = sum(arr[i+ 2][j:j + 3])
                    # sum up the hourglass
                    total = first_row + mid_row + last_row
                    print(f'total: {total}')
                    my_list.append(total)

    return max(my_list)


##### SOL 2 ###
# hourglass can only be created with 3 rows
# the last two rows and columns cannot be used to create the hourglass (7) values
# our range for the outer and inner loop is len the arr -2
# iterate and append the hourglass vals into a list 
# we then get the the sum of the top row (3)
# get the mid value
# get the sum of the last row 
# sum of all the rows in hourglass
# append the total of the hourglass to the list
# return the max value of the list
def hourglassSum2(arr):
    my_list = []

    for i in range(len(arr) -2):
        for j in range(len(arr[i])-2):
            first_row = sum(arr[i][j:j + 3])
            mid_row = sum(arr[i + 1])
            last_row = sum(arr[i+ 2][j:j + 3])
            total = first_row + mid_row + last_row
            my_list.append(total)

    return max(my_list)



# every 3 columns and 3 rows is an hour glass (4 in each row)
arr = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0,],
    [0,0,0,0,0,0,],
]
print(f'max value: {hourglassSum2(arr)}')