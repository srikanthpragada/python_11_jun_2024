source = "names.txt"
target = "newnames.txt"

with( open("names.txt", "rt") as sf,
      open("newnames.txt", "wt") as tf):
    tf.write(sf.read())
