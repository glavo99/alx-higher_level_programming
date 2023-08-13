#!/usr/bin/python3

def element_at(my_list, idx):
    ranger = len(my_list) - 1
    if idx < 0 or ranger < idx:
        return None
    else:
        return (my_list[idx])
