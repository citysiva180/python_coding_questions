def is_sorted(given_list):
    # very important expression!
    return all(given_list[index] <= given_list[index + 1] for index in range(len(given_list) - 1))


# Example usage
numbers = [10, 20, 30, 40]
print(is_sorted(numbers))  # Output: True

numbers = [10, 20, 15, 30]
print(is_sorted(numbers))  # Output: False
