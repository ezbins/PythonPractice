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


class Athlete:

    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([formatter(t) for t in self.times]))[0:3])

sarah = Athlete('Sarah Sweeney', '2006-07-19',
                ['2:58', '2.34', '1.89', '1:56'])

print(type(sarah))
print(sarah.name)
print(sarah.times)
print(sarah.top3())
