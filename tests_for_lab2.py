def sum_in_massive(array, P):
    array.sort()
    for i in range(len(array) - 2):
        left, right = i + 1, len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == P:
                return True
            elif sum < P:
                left += 1
            else:
                right -= 1
    return False
