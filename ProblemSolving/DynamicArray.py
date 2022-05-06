def dynamicArray(n, queries):
    my_list = []
    answers = []
    last_answer = 0

    # create dynamic 2d arr of n empty arrays
    for i in range(n):
        my_list.append([])
    
    # go through queries arr
    for i in range(len(queries)):
        x = queries[i][1]
        y = queries[i][2]
        idx = ((x ^ last_answer) % n)

        if queries[i][0] == 1: # query type 1
            my_list[idx].append(y)
                
        elif queries[i][0] == 2: # query type 2
            last_answer = my_list[idx][y % len(my_list[idx])]
            answers.append(last_answer)

    return answers


n = 3
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
print(f'{dynamicArray(n,queries)}')