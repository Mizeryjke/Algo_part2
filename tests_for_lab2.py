def my_merge(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half_massive = array[:mid]
        right_half_massive = array[mid:]

        my_merge(left_half_massive)
        my_merge(right_half_massive)

        i = j = k = 0

        while i < len(left_half_massive) and j < len(right_half_massive):
            if left_half_massive[i] < right_half_massive[j]:
                array[k] = left_half_massive[i]
                i += 1
            else:
                array[k] = right_half_massive[j]
                j += 1
            k += 1

        while i < len(left_half_massive):
            array[k] = left_half_massive[i]
            i += 1
            k += 1

        while j < len(right_half_massive):
            array[k] = right_half_massive[j]
            j += 1
            k += 1

def sum_in_massive(array, summa_of_3):
    my_merge(array)
    for i in range(len(array) - 2):
        left, right = i + 1, len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == summa_of_3:
                return True
            elif sum < summa_of_3:
                left += 1
            else:
                right -= 1
    return False
