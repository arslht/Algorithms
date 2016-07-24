def find-max-crossing-subbarray(A,low,mid,high):
    """
    left - sum = -∞
    sum = 0
    for i = mid downto low
        sum = sum + A[i]
        if sum > left-sum
            left - sum = sum
            max - left = sum
    right - sum = -∞
    sum = 0
    for j = mid + 1 to high
        sum = sum + A[i]
        if sum > right - sum
            right - sum = sum
            max - right = j
    return (max-left, max-right, left-sum, left+sum)
    """

    print
    return 

def find-max-subarray(A,low,high):
    """
    if high == low
        return (low,high,A[low])
    else mid=取整（(low+high)/2）
        (left-low, left-high, left-sum) = find-max-subarray(A,low,mid)
        (right-low, right-high, right-sum) = find-max-subarray(A,mid+1,high)
        (cross-low, cross-high, cross-sum) = find-max-crossing-subarray(A,low,mid,high)
    if left-sum >= right-sum and left-sum >= cross-sum
        return (left-low, left-high, left-sum)
    elseif right-sum >= left-sum and right-sum >= cross-sum
        return (right-low, right-high, right-sum)
    else retrun (cross-low, cross-high, cross-sum)
    """

    print
    return

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]