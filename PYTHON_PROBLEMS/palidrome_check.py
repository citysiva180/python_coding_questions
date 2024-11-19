from typing import List
# Forward Recursion!


def recursive_reverse_string(word):

    reverse_string_list = []
    count = len(word)-1

    def reversal_recursion(count):

        if count < 0:
            return
        reverse_string_list.append(word[count])
        reversal_recursion(count-1)

    reversal_recursion(count)

    reversed_string = "".join(reverse_string_list)
    print(reversed_string)
    if word == reversed_string:
        print("True")
        return True

    else:
        print("False")
        return False


word = "abbba"
recursive_reverse_string(word)
word_1 = "Niko"
recursive_reverse_string(word_1)


# def hello_world(count=0, n=12):
#     if count > n:  # Base case: Stop recursion
#         return
#     print(count)
#     print("Hello_world! - ", count)
#     hello_world(count + 1, n)  # Recursive call with incremented count


# hello_world()

# # Reverse Recursion


# def hello_world(n=12):
#     if n <= 0:  # Base case: Stop recursion
#         return
#     print("Hello_world! - ", n)

#     # Recursive call with incremented count | Remember to add it here..
#     hello_world(n-1)


# hello_world()
