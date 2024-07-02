def unique_chars(*names):
    allchars = "".join(names)    # concatenate all names
    uniquechars = set(allchars)  # str to set
    return "".join(sorted(uniquechars))  # set to str


print(unique_chars('Java', 'Python', 'SQL', 'Php'))
