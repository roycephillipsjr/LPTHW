formatter = " {} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# my own practice with this formatter.format()

print(formatter.format(5, 6, 7, 8))
print(formatter.format(
    "My baby don't come around",
    "Unless she knows for sure",
    "That she will be so cool",
    "Baby"))

print(formatter.format(formatter, formatter, formatter, formatter))


lines = (
    "Try your"
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>TEST\n", repr(lines))
