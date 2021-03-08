"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):

    incoming_list.sort()

    print(max(incoming_list))

    pass


def find_least_number(incoming_list):

    incoming_list.sort()

    print(min(incoming_list))
    pass


def add_list_numbers(incoming_list):

    incoming_list.sort()

    print(sum(incoming_list))

    pass


def longest_value_key(incoming_dict):

    longest_word = max(len(incoming_dict))
    return longest_word

    pass
