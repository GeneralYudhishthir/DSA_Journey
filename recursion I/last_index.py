def last_index(nums,x,i=0):
    if i == len(nums):
        return -1
    
    print("*")
    smallans = last_index(nums,x,i+1)
    if smallans != -1:
        return smallans
    
    elif nums[i] == x:
        return i
    

print(last_index([1,2,3,1],1))