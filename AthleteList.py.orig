#!/usr/bin/python3


class Athlete(list):

   def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])  # put here
        self.name = a_name
        self.times = a_times
        self.dob = a_dob

    def formatter(self, String_pattrn):
        if '-' in String_pattrn:
            split_formatter = '-'
        elif ':' in String_pattrn:
            split_formatter = ':'
        else:
            return String_pattrn

        (mins, secs) = String_pattrn.split(split_formatter)
        return(mins + "." + secs)

    def top3(self):
        return(sorted(set([self.formatter(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)
