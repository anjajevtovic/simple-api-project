
try:
    int("a")
except ValueError as e:
    print("oops, do not do that", e)