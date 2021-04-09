"""
author: Praful
code: Binary Search
"""


def binary_search(item, sorted_list):
    """
    given an item to find and a sorted list,
    search the item in the list and
    reutrn the position of the item in the list
    :param item: item to search
    :param sorted_list: sorted list (Binary search always requires sorted list)
    :return: position/None based on found or not
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess_number = sorted_list[mid]

        if guess_number == item:
            return mid
        if guess_number > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":

    search_item = 1
    search_in_list = [1, 3, 5, 7, 9, 10]
    res = binary_search(search_item, search_in_list)
    print(res)