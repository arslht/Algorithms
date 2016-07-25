def find_max_crossing_subarray(A,low,mid,high):
    (left-sum) = -float("inf")
    sum = 0
    for i in range(mid,low-1):
        sum += A[i]
        if sum > left-sum:
            left-sum = sum
            max-left = sum

    right-sum = -float("inf")
    sum = 0
    for j in range(mid+1,high+1):
        sum = sum + A[j]
        if sum > right-sum:
            right-sum = sum
            max-right = j
    return (max-left, max-right, left-sum, left+sum)

def find_max_subarray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else: 
        mid=int((low+high)/2)
        (left-low, left-high, left-sum) = find_max_subarray(A,low,mid)
        (right-low, right-high, right-sum) = find_max_subarray(A,mid+1,high)
        (cross-low, cross-high, cross-sum) = find_max_crossing_subarray(A,low,mid,high)
    if left-sum >= right-sum and left-sum >= cross-sum:
        return (left-low, left-high, left-sum)
    elif right-sum >= left-sum and right-sum >= cross-sum:
        return (right-low, right-high, right-sum)
    else: 
        retrun (cross-low, cross-high, cross-sum)

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print (find_max_subarray(A,0,len(A)-1))
