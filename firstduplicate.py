def firstDuplicate(array):
    """
    Time O(n) | Space O(n)
    """
    dic = {}
    for num in array:
        if num in dic:
            return num
        else:
            dic[num] = True
    return -1
print(firstDuplicate([2,1,3,5,3]))