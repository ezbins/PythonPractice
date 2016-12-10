#!/usr/bin/env python3

import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.rt(90)
        
    turtle.mainloop()

bob = turtle.Turtle()
square(bob)

