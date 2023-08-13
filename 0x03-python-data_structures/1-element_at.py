#!/usr/bin/python3
def element_at(my_list, idx):
    ranger = len(my_list)
    if idx < 0 or ranger == 0 or idx >= ranger:
        return("None")
    else:
        return(my_list[idx])
