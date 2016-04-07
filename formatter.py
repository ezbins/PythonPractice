#!/usr/bin/python3


def formatter(String_pattrn):
    if '-' in String_pattrn:
        split_formatter = '-'
    elif ':' in String_pattrn:
        split_formatter = ':'
    else:
        return String_pattrn

    (mins, secs) = String_pattrn.split(split_formatter)

    return(mins + "." + secs)

old_list = ['2:30', '4:20', '1.70', '3-50', '5-60']
new_list = []

for item in old_list:
    new_list.append(formatter(item))

print(new_list)
