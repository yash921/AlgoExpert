def productSum(array, multiplier = 1):
    sum = 0
    for num in array:
        if type(num) is list:
            sum += productSum(num, multiplier + 1)
        else:
            sum += num
    return sum * multiplier

print(productSum([5,2,[7,-1],3,[6,[-13,8],4]]))         
