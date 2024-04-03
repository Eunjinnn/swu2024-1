words = ""
for n in input():
    if n.isupper():
        words += n.lower()
    else:
        words += n.upper()

print(words)
