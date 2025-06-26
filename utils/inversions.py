def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) < 2:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        result = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv_count += len(left) - i
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions
