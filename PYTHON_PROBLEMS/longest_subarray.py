def longest_subarray_with_sum_k(array, array_length, target_sum):
    # Dictionary to store prefix sums and their first occurrences
    prefix_sum_indices = {}

    # Initialize variables
    prefix_sum = 0
    longest_subarray_length = 0

    for index in range(array_length):
        # Update the prefix sum
        prefix_sum += array[index]

        # If the prefix sum itself equals the target, update the length
        if prefix_sum == target_sum:
            longest_subarray_length = max(longest_subarray_length, index + 1)

        # Check if the difference (prefix_sum - target_sum) exists in the hashmap
        difference = prefix_sum - target_sum
        if difference in prefix_sum_indices:
            # Calculate the subarray length
            subarray_length = index - prefix_sum_indices[difference]
            longest_subarray_length = max(
                longest_subarray_length, subarray_length)

        # Store the first occurrence of the prefix sum in the hashmap
        if prefix_sum not in prefix_sum_indices:
            prefix_sum_indices[prefix_sum] = index

    return longest_subarray_length


# Example usage
n = 7
k = 3
a = [1, 2, 3, 1, 1, 1, 1]
result = longest_subarray_with_sum_k(a, n, k)
print("Length of the longest subarray with sum =", k, "is", result)
