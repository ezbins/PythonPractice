import os

try:
    out = open('bewrite1.file', "w")
    print("writing something...", file=out)
    print("writing something again", file=out)

except IOError:
    print("Can not open file.")
finally:
    out.close()
