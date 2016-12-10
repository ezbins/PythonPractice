#!/usr/bin/env python3


def do_twice(f, arg):
    f(arg)
    f(arg)


def print_spam(arg):
    print(arg)


def print_twice(arg):
    print(arg)
do_twice(print_spam, 'two args')

do_twice(print_twice, 'print_twice')
