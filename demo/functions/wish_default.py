def wish(name="Guest", message="Hi"):
    print(message, name)


# Positional args
wish("Scott")
wish("Tom", "Hello")
wish()

# Keyword args
wish(name="Dave")
wish(message="Good Morning", name="Steve")
wish(message="Hello")
