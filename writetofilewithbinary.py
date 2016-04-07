#import os
import pickle

try:
    with open('bewrite1.file', "wb") as out:
        pickle.dump("12434",out)
        # print("writing something...", file=out)
        # print("writing something again", file=out)
    with open('bewrite1.file',"rb") as readin:
      content = pickle.load(readin)
      print(content)
except IOError:
    print("Can not open file.")
