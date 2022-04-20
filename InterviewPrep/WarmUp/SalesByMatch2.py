def sockMerchant(n: int, ar: list) -> int:
    tmp_dict = {}
    pairs_list = []

    for x in range(0,n):

        # check if the pair is in the dict
        if ar[x] not in tmp_dict:
            tmp_dict[ar[x]] = 1
        # increase number of occurences in dict when element has already been seen
        elif ar[x] in tmp_dict:
            tmp_count = tmp_dict[ar[x]]
            tmp_count +=1
            tmp_dict[ar[x]] = tmp_count

        # after the last element has been seen get all the pairs in the arr
        if x == n -1:
            for key in tmp_dict.keys():
                if int(tmp_dict[key]/2) > 0:
                    pairs_list.append(int(tmp_dict[key]/2))

    return sum(pairs_list)


ar = [10,20,20,10,10,30,50,10,20]
n = 9
print(sockMerchant(n,ar))