#binary search 
#method 1

#time complexity: 0(log n)
#condition: binary search works with ordered list

#method; recursive

def binary_search(arr,low,upper,finding_element):
    mid = (low+upper) // 2 #floor division of 2 (middle point considered first index number) example if 3/2 is 1.5 floor division will  only give 1, decimal is neglected
    if low <=upper:
        if arr[mid] == finding_element:
            return mid #mid value returned
        elif arr[mid] < finding_element: #looking in the second half of list so low = mid+1
            return binary_search(arr,mid+1, upper, finding_element)
        else: 
            return binary_search(arr, mid-1, low, finding_element)
    else:
        return -1
        
print(binary_search([1,2,3,4,5,6,7], 0, 6, 5))

#method 2


