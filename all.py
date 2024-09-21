# Advanced Operations on Python Lists

# Task 1: Creating a List of Squares Using List Comprehension
def squares_list(n):
    """
    Creates a list of squares of numbers from 1 to n using list comprehension

    :param n: The upper bound of the range (inclusive).
    :retuen: A list of squares from 1 to n.

    """

    return [i ** 2 for i in range(1, n + 1)]

# Task 2: Reversing a Sublist Within a List
def reverse_sublist(lst, i, j):
    """
    Reverse a sublist within the list 1st from index i to j (inclusive).
    
    :param 1st: The list in which the sublist will be reversed.
    :param i: The starting index of the sublist.
    :param j: The ending index of the sublist.
    :return: The list with the sublist reversed.

    """
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# Example usage
lst = [1, 2, 3, 4, 5, 6]
print(reverse_sublist(lst, 1, 4))  # Output: [1, 5, 4, 3, 2, 6]

# Task 3: Merging Two Sorted Lists
def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into s single sorted list.

    :param list1: The first sorted list.
    :param list2: The second sorted list.
    :return: A new sorted list containing all elements of list1 and list2.

    merged_list = [] # Initialize an empty list for the merged result
    i, j, = 0, 0 # initialize pointers for both lists

    # Traverse both lists and merge them
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j +=
    # Append any remaining elements from list1 or list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

    # Example usage
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    print(merge_sorted_lists(list1, list2)) # Output: [1, 2, 3, 4, 5, 6]

    """

# Dictionary Manipulation and Optimization

# Task 1: Merging two dictionaries
def merge_dictionaries(dict1, dict2):
    # Create a copy of dict1 to avoid modifying the orginal
    merged_dict = dict1.copy()
    # Update with dict2, preserving values from dict2 for common keys
    merged_dict.update(dict2)
    return merged_dict
# Task 2: Intersection of two dictionaries
def intersect_dictionaries(dict1, dict2):
    # Create a dictionary for common keys
    intersection = {key: dict1[key] for key in dict1 if key in dict2}
    return intersection 
    
# Task 3: Word frequncy counter
def word_frequency(words):
        # Initialize an empty dictionary to store word counts
    freq_dict = {}
    for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
    return freq_dict

# Example usage
if __name__ == "__main__":
    # Task 1 Example
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 5, 'd': 6}
    print("Merged Dictionary:", merge_dictionaries(dict1, dict2))
    
    # Task 2 Example
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 5, 'd': 6}
    print("Intersection of Dictionaries:", intersect_dictionaries(dict1, dict2))
    
    # Task 3 Example
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'orange']
    print("Word Frequency:", word_frequency(words))