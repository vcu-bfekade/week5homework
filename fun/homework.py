"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    maxiumum = max(incoming_list)
    return maxiumum


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    least = min(incoming_list)
    return least


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    list_sum = 0
    if incoming_list is None or len(incoming_list) == 0:
        list_sum = 0
    else:
        list_sum = sum(incoming_list)
    return list_sum


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    highest = incoming_dict
    if highest is not None:
        if len(highest) == 0:
            return 0
        else:
            return max(highest, key=lambda m: len(highest[m]))
